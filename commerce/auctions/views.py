from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django import forms

from .models import Category, Listings, User, Comments, Bids



class ListingForm(forms.Form):
    product = forms.CharField(max_length=60)
    description = forms.CharField(max_length=500)
    price = forms.FloatField()
    url = forms.CharField(max_length=500)

def index(request):
    listings = Listings.objects.filter(isActive=True)

    return render(request, "auctions/index.html", {
        "listings": listings,
        "categories": Category.objects.all()
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

@login_required()
def create_listing(request):
    if request.method == "GET":
        form =ListingForm()
        return render(request, "auctions/create_listing.html", {
            "form": form,
            "categories": Category.objects.all()
        })
    else:
        form = ListingForm(request.POST)
        if form.is_valid():
            product = form.cleaned_data['product']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            url = form.cleaned_data['url']
            category = request.POST["category"]

            # Get current user
            current_user = request.user

            # Get a selected category
            category_data = Category.objects.get(categoryName=category)

            # Create a bid object
            bid = Bids(bid=float(price), user = current_user)
            bid.save()

            #Create a new form
            new_listing = Listings(
                title = product,
                description = description,
                price = bid,
                imageUrl = url,
                owner = current_user,
                category = category_data
            )

            # Insert form in our database
            new_listing.save()

            return HttpResponseRedirect(reverse('index'))

def display_categories(request):
    if request.method == "POST":
        category_form = request.POST['category']
        category = Category.objects.get(categoryName=category_form)
        listings = Listings.objects.filter(isActive=True, category=category)
        return render(request, "auctions/index.html", {
            "listings": listings,
            "categories": Category.objects.all()
        })

def listing(request, id):
    listing = Listings.objects.get(pk=id)
    listing_in_watchlist = request.user in listing.watchlist.all()
    all_comments = Comments.objects.filter(listing=listing)
    is_owner = request.user.username == listing.owner.username
    return render(request, "auctions/listing.html", {
        'listing': listing,
        'in_watchlist': listing_in_watchlist,
        'all_comments': all_comments,
        'is_owner': is_owner
    })   

def remove_watchlist(request, id):
    listing = Listings.objects.get(pk=id)
    current_user = request.user
    listing.watchlist.remove(current_user)
    return HttpResponseRedirect(reverse("listing", args=(id, )))

def add_watchlist(request,id):
    listing = Listings.objects.get(pk=id)
    current_user = request.user
    listing.watchlist.add(current_user)
    return HttpResponseRedirect(reverse("listing", args=(id, )))

def display_watchlist(request):
    current_user = request.user
    listings = current_user.user_watchlist.all()
    return render(request, "auctions/watchlist.html", {
        'listings': listings
    })

def add_comment(request, id):
    current_user = request.user
    listing = Listings.objects.get(pk=id)
    message = request.POST['new_comment']

    new_comment = Comments(
        author = current_user,
        listing = listing,
        message = message
    )

    new_comment.save()

    return HttpResponseRedirect(reverse("listing", args=(id, )))

def add_bid(request, id):
    new_bid = request.POST['new_bid']
    listing = Listings.objects.get(pk=id)
    listing_in_watchlist = request.user in listing.watchlist.all()
    all_comments = Comments.objects.filter(listing=listing)
    is_owner = request.user.username == listing.owner.username
    if int(new_bid) > listing.price.bid:
        update_bid = Bids(user=request.user, bid=int(new_bid))
        update_bid.save()
        listing.price = update_bid
        listing.owner = request.user
        listing.save()
        is_owner = request.user.username == listing.owner.username
        return render(request, "auctions/listing.html", {
            "listing": listing,
            "message": "Bid was updated successfully",
            "update": True,
            'in_watchlist': listing_in_watchlist,
            'all_comments': all_comments,
            'is_owner': is_owner
            
        })
    else:
        return render(request, "auctions/listing.html", {
            "listing": listing,
            "message": "Bid was not updated",
            "update": False,
            'in_watchlist': listing_in_watchlist,
            'all_comments': all_comments,
            'is_owner': is_owner
        })

def close_auction(request, id):
    listing = Listings.objects.get(pk=id)
    listing.isActive = False
    listing.save()
    listing_in_watchlist = request.user in listing.watchlist.all()
    all_comments = Comments.objects.filter(listing=listing)
    is_owner = request.user.username == listing.owner.username
    return render(request, "auctions/listing.html", {
            "listing": listing,
            "message": "Kuddos! Your auction is closed",
            "update": True,
            'in_watchlist': listing_in_watchlist,
            'all_comments': all_comments,
            'is_owner': is_owner
        })
    