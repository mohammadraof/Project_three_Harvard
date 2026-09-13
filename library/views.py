from django.shortcuts import render
from .sample_data import books, members


def home(request):
    return render(request, "library/home.html")


def book_list(request):
    query = request.GET.get("q", "").strip().lower()
    status = request.GET.get("status", "").strip().lower()

    filtered_books = books

    #Search by title or author
    
    if query:
        filtered_books = [
            book
            for book in filtered_books
            if query in book["title"].lower()
            or query in book["author"].lower()
        ]

    # Filter by book status

    if status == "available":
        filtered_books = [
            book
            for book in filtered_books
            if book["available"] is True
        ]

    elif status == "borrowed":
        filtered_books = [
            book
            for book in filtered_books
            if book["available"] is False
        ]

    return render(request, "library/book_list.html", {
        "books": filtered_books,
        "query": query,
        "status": status,
    })


def member_list(request):
    return render(request, "library/member_list.html", {
        "members": members,
    })


def statistics(request):
    total_books = len(books)
    total_members = len(members)
    available_books = len([
        book for book in books
        if book["available"]
    ])

    return render(request, "library/statistics.html", {
        "total_books": total_books,
        "total_members": total_members,
        "available_books": available_books,
    })