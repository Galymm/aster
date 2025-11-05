from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Card, Category
from .forms import CardForm, CategoryForm

def home(request):
    query = request.GET.get('q', '')
    category_name = request.GET.get('category', '')
    subcategory_name = request.GET.get('subcategory', '')

    categories = Category.objects.filter(parent__isnull=True)
    cards = Card.objects.all()

    if query:
        cards = cards.filter(
            Q(question__icontains=query) |
            Q(answer__icontains=query) |
            Q(category__name__icontains=query)
        )

    if category_name:
        cards = cards.filter(
            Q(category__name=category_name) | Q(category__parent__name=category_name)
        )

    if subcategory_name:
        cards = cards.filter(category__name=subcategory_name)

    return render(request, 'cards/home.html', {
        'cards': cards.distinct(),
        'categories': categories,
        'selected_category': category_name,
        'selected_subcategory': subcategory_name,
    })


# ---- КАРТОЧКИ ----
def add_card(request):
    if Category.objects.count() == 0:
        return render(request, 'cards/no_category.html')

    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CardForm()

    return render(request, 'cards/add_card.html', {'form': form})


def edit_card(request, card_id):
    card = get_object_or_404(Card, id=card_id)
    if request.method == 'POST':
        form = CardForm(request.POST, instance=card)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CardForm(instance=card)
    return render(request, 'cards/edit_card.html', {'form': form})


def delete_card(request, card_id):
    card = get_object_or_404(Card, id=card_id)
    card.delete()
    return redirect('home')


# ---- КАТЕГОРИИ ----
def add_category(request, parent_id=None):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CategoryForm(initial={'parent': parent_id})
    return render(request, 'cards/add_category.html', {'form': form})


def edit_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'cards/edit_category.html', {'form': form, 'category': category})


def delete_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        category.delete()
        return redirect('home')
    return render(request, 'cards/delete_category.html', {'category': category})
