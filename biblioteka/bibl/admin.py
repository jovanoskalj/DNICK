from django.contrib import admin
from .models import Genre, Translator, Book, Rating, BookGenre, BookTranslator

class BookGenreInline(admin.TabularInline):
    model = BookGenre
    extra = 1

class BookTranslatorInline(admin.TabularInline):
    model = BookTranslator
    extra = 1

class RatingInline(admin.TabularInline):
    model = Rating
    extra = 1
    readonly_fields = ('user', 'rating', 'comment', 'created_at')
    can_delete = True

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish_date', 'added_by', 'page_count', 'is_available', 'average_rating_display')
    list_filter = ('is_available',)
    search_fields = ('title', 'author')
    inlines = [BookGenreInline, BookTranslatorInline, RatingInline]

    def average_rating_display(self, obj):
        avg = obj.average_rating()
        return round(avg, 2) if avg else "No ratings"
    average_rating_display.short_description = 'Avg. Rating'

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(Translator)
class TranslatorAdmin(admin.ModelAdmin):
    list_display = ('name', 'nationality', 'birth_date')

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'rating', 'created_at')
    search_fields = ('book__title', 'user__username')
    list_filter = ('rating',)

@admin.register(BookGenre)
class BookGenreAdmin(admin.ModelAdmin):
    list_display = ('book', 'genre')

@admin.register(BookTranslator)
class BookTranslatorAdmin(admin.ModelAdmin):
    list_display = ('book', 'translator')
