from django.shortcuts import render, redirect
from .sample_data import books, members, borrowings
from datetime import date




# ------------------
# FIND book
# ------------------

def find_book(book_id):
    return next((b for b in books if b["id"] == book_id), None)

# ------------------
# FIND MEMBER
# ------------------

def find_member(member_id):
    return next((m for m in members if m["id"] == member_id), None)

# ------------------
# BORROW BOOK
# ------------------

def borrow_book(request, book_id, member_id):
    book = find_book(book_id)
    member = find_member(member_id)

    if request.method == "POST" and book and member and book["available"]:
        book["available"] = False
        book["borrow_count"] += 1

        borrowings.append({
            "book_id": book_id,
            "member_id": member_id,
            "borrowed_at": date.today().isoformat(),
            "returned_at": None,
        })

    return redirect("book_list")


# ------------------
# RETURN BOOK
# ------------------

def return_book(request, book_id):
    book = find_book(book_id)

    if request.method == "POST" and book and not book["available"]:
        book["available"] = True

        for borrowing in borrowings:
            if(
                borrowing["book_id"] == book_id
                and borrowing["returned_at"] is None
            ):
                borrowing["returned_at"] = date.today().isoformat()
                break
    
    return redirect("book_list")


# ------------------
# HISTORY
# ------------------

def history(request, member_id):
    member = find_member(member_id)

    member_borrowings = []

    for borrowing in borrowings:
        if borrowing["member_id"] == member_id:
            member_borrowings.append(borrowing)

    return render(
        request,
        "library/history.html",
        {
            "member": member,
            "borrowings": member_borrowings,
            "books": books,
        },
    )

# ------------------
# HOME
# ------------------

def home(request):
    return render(request, "library/home.html")

# ------------------
# BOOK LIST
# ------------------
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

# ------------------
# MEMBER LIST
# ------------------

def member_list(request):
    return render(request, "library/member_list.html", {
        "members": members,
    })

# ------------------
# STATISTICS
# ------------------

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