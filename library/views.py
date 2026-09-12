from django.shortcuts import render
from .sample_data import books, members, borrowings

# Create your views here.
def home(request):
    return render(request, "library/home.html")

# -----------------
# BOOK LIST
# -----------------
def book_list(request):
    query = request.GET.get("q", "").strip().lower()
    filtered_books = books

    if query:
        filtered_books = [
            book for book in books
            if query in book["title"].lower()
            or query in book["author"].lower()
        ]

    return render(request, "library/book_list.html", {
        "books": filtered_books,
        "query": query,
    })

# -----------------
# MEMBER LIST
# -----------------
def member_list(request):
    return render(request, "library/member_list.html", {
        "members": members,
    })

# -----------------
# STATISTICS
# -----------------
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