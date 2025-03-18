from django.contrib import admin
from .models import Translator, Genre, Book, Author, BookGenres, BookAuthors, BookTranslators, Rating


class RatingInline(admin.TabularInline):
    exclude = ("user",)
    model = Rating
    readonly_fields = ("user",)
    extra = 2
    def has_change_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        # if obj is None or request.user != obj.added_by:
        #     return True
        # return any(rating.user == request.user for rating in obj.rating_set.all())
        return True
    def has_add_permission(self, request, obj=None):
        if obj is None or request.user != obj.added_by:
            return True
        return request.user != obj.added_by
        # i want to set the user of the rating object to be the user from the request, but rating is inline


class BookGenresInline(admin.TabularInline):
    model = BookGenres
    extra = 1

    def has_change_permission(self, request, obj=None):
        if obj is None or request.user == obj.added_by:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if obj is None or request.user == obj.added_by:
            return True
        return False

    def has_add_permission(self, request, obj=None):
        if obj is None or request.user == obj.added_by:
            return True
        return False

class BookAuthorsInline(admin.TabularInline):
    model = BookAuthors
    extra = 1

    def has_change_permission(self, request, obj=None):
        if obj is None or request.user == obj.added_by:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if obj is None or request.user == obj.added_by:
            return True
        return False

    def has_add_permission(self, request, obj=None):
        if obj is None or request.user == obj.added_by:
            return True
        return False

class BookTranslationsInline(admin.TabularInline):
    model = BookTranslators
    extra = 1
    def has_change_permission(self, request, obj=None):
        if obj is None or request.user == obj.added_by:
            return True
        return False
    def has_delete_permission(self, request, obj=None):
        if obj is None or request.user == obj.added_by:
            return True
        return False

    def has_add_permission(self, request, obj=None):
        if obj is None or request.user == obj.added_by:
            return True
        return False

class BookAdmin(admin.ModelAdmin):
    exclude = ("added_by",)
    list_display = ("title", "issue_date", "added_by", "available",)
    list_filter = ("available",)
    inlines = [BookGenresInline, BookAuthorsInline, BookTranslationsInline, RatingInline]

    def get_readonly_fields(self, request, obj=None):
        if obj is None or obj.added_by == request.user:
            return []
        return ["title", "issue_date", "added_by", "available", "book_cover", "num_pages",]

    # def has_change_permission(self, request, obj=None):
    #     if obj is None:
    #         return True
    #     return obj.added_by == request.user

    def has_delete_permission(self, request, obj=None):
        if obj is None:
            return True
        return obj.added_by == request.user

    def save_model(self, request, obj, form, change):
        if not change:
            obj.added_by = request.user
        obj.save()
        return super(BookAdmin, self).save_model(request, obj, form, change)

    def save_formset(self, request, form, formset, change):
        """Ensure Rating objects get the current user as the 'user' field, and allow deletions."""
        instances = formset.save(commit=False)  # Get unsaved inline instances

        # Handle newly added instances
        for instance in instances:
            if isinstance(instance, Rating) and not instance.pk:
                instance.user = request.user  # Assign current user
            instance.save()  # Save each instance

        # Handle deleted instances
        for obj in formset.deleted_objects:
            obj.delete()  # Explicitly delete removed objects

        formset.save_m2m()  # Save many-to-many relationships if any


admin.site.register(Translator)
admin.site.register(Genre)
admin.site.register(Book, BookAdmin)
admin.site.register(Author)