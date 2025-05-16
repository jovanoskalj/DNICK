
public async Task<IActionResult> AddChapters(Guid bookId)
{
    var book = _context.Books.FirstOrDefault(b => b.Id == bookId);
    if (book == null)
        return NotFound();

    using var client = new HttpClient();
    var request = new { bookId = bookId.ToString() };
    var json = JsonSerializer.Serialize(request);
    var content = new StringContent(json, Encoding.UTF8, "application/json");

    var response = await client.PostAsync("http://is-lab4.ddns.net:8080/chapters", content);
    if (!response.IsSuccessStatusCode)
        return View("Error");

    var result = await response.Content.ReadAsStringAsync();
    var chaptersDto = JsonSerializer.Deserialize<List<ChapterDto>>(result, new JsonSerializerOptions { PropertyNameCaseInsensitive = true });

    var chapters = chaptersDto.Select(dto => new Chapter
    {
        Id = Guid.NewGuid(),
        BookId = book.Id,
        Title = dto.Title,
        PageCount = dto.PageCount,
        Summary = dto.Summary,
        ChapterNumber = dto.ChapterNumber,
        HasExercises = dto.HasExercises,
        KeyConcept = dto.KeyConcept,
        DifficultyLevel = dto.DifficultyLevel,
        LastUpdated = dto.LastUpdated
    }).ToList();

    _context.Chapters.AddRange(chapters);
    await _context.SaveChangesAsync();

    return RedirectToAction("Details", new { id = book.Id });
}


public async Task<IActionResult> FetchBooks()
{
    using var client = new HttpClient();
    var response = await client.GetAsync("http://is-lab4.ddns.net:8080/books");
    if (!response.IsSuccessStatusCode)
        return View("Error");

    var content = await response.Content.ReadAsStringAsync();
    var bookDtos = JsonSerializer.Deserialize<List<BookDto>>(content, new JsonSerializerOptions { PropertyNameCaseInsensitive = true });

    var books = bookDtos.Select(dto => new Book
    {
        Id = Guid.NewGuid(),
        Title = dto.Name,
        ISBN = dto.IsbnCode,
        Description = dto.ShortDescription,
        Author = $"{dto.AuthorFirstName} {dto.AuthorLastName}",
        PublishedYear = dto.PublishedYear
    }).ToList();

    _context.Books.AddRange(books);
    await _context.SaveChangesAsync();

    return RedirectToAction("Index");
}




ovde
// Display Books – прикажи книги од API
public async Task<IActionResult> DisplayBooks()
{
    using var client = new HttpClient();
    var response = await client.GetAsync("http://is-lab4.ddns.net:8080/books");
    if (!response.IsSuccessStatusCode)
        return View("Error");

    var content = await response.Content.ReadAsStringAsync();
    var books = JsonSerializer.Deserialize<List<BookDto>>(content, new JsonSerializerOptions { PropertyNameCaseInsensitive = true });
    
    return View("BooksFromApi", books);
}


// Display Books – прикажи книги од API
public async Task<IActionResult> DisplayBooks()
{
    using var client = new HttpClient();
    var response = await client.GetAsync("http://is-lab4.ddns.net:8080/books");
    if (!response.IsSuccessStatusCode)
        return View("Error");

    var content = await response.Content.ReadAsStringAsync();
    var books = JsonSerializer.Deserialize<List<BookDto>>(content, new JsonSerializerOptions { PropertyNameCaseInsensitive = true });
    
    return View("BooksFromApi", books);
}



@model List<BookDto>

<h2>Books from External API</h2>

<table class="table">
    <thead>
        <tr>
            <th>Title</th>
            <th>Author</th>
            <th>ISBN</th>
            <th>Description</th>
            <th>Year</th>
        </tr>
    </thead>
    <tbody>
        @foreach (var book in Model)
        {
            <tr>
                <td>@book.Name</td>
                <td>@book.AuthorFirstName @book.AuthorLastName</td>
                <td>@book.IsbnCode</td>
                <td>@book.ShortDescription</td>
                <td>@book.PublishedYear</td>
            </tr>
        }
    </tbody>
</table>



// Display Books – прикажи книги од API
public async Task<IActionResult> DisplayBooks()
{
    using var client = new HttpClient();
    var response = await client.GetAsync("http://is-lab4.ddns.net:8080/books");
    if (!response.IsSuccessStatusCode)
        return View("Error");

    var content = await response.Content.ReadAsStringAsync();
    var books = JsonSerializer.Deserialize<List<BookDto>>(content, new JsonSerializerOptions { PropertyNameCaseInsensitive = true });
    
    return View("BooksFromApi", books);
}




// BookDto.cs
public class BookDto
{
    public int Id { get; set; }
    public string Name { get; set; }
    public string AuthorFirstName { get; set; }
    public string AuthorLastName { get; set; }
    public string IsbnCode { get; set; }
    public string ShortDescription { get; set; }
    public int PublishedYear { get; set; }
}

// ChapterDto.cs
public class ChapterDto
{
    public string Title { get; set; }
    public int PageCount { get; set; }
    public string Summary { get; set; }
    public int ChapterNumber { get; set; }
    public bool HasExercises { get; set; }
    public string KeyConcept { get; set; }
    public string DifficultyLevel { get; set; }
    public DateTime LastUpdated { get; set; }
}

Даден е почетен код во кој е имплементирано едностано решение за чување податоци за книги (Book) и нивни делови (Chapter). Ваша задача е да го проширите постоечкиот проект така што ќе овозможите повици до API-то (http://is-lab4.ddns.net:8080)
При клик на копчето Display Books на страницата /Books, ќе се направи GET повик до /books при што во ново View ќе ги излистате книгите кои ги враќа API-то со сите детали  
При клик на копчето Fetch Books на страницата /Books, ќе се направи GET повик до /books при што книгите кои ги враќа API-то ќе ги мапирате во моделот Book и како такви ќе ги запишете во базата на податоци. Внимавајте на соодветно мапирање на атрибутите. Во моделот Book, името и презимето на авторот се чуваат конкатанирани во рамки на еден string
При клик на копчето Add Chapters на страницата /Books за соодветна книга, ќе се направи POST повик до /chapters при што деловите кои ги враќа API-то ќе ги мапирате во моделот Chapter и ќе ја креирате релацијата со книгата на која се однесува повикот.
За секоја од задачите постои веќе креирана акција во BooksController.

API документацијата е достапна на следниот линк:

http://is-lab4.ddns.net:8080/swagger-ui/index.html

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.Json;
using System.Threading.Tasks;

namespace BookApplication.Domain.DomainModels
{
    public class Chapter : BaseEntity
    {
        public Guid BookId { get; set; }
        public Book? Book { get; set; }
        public string Title { get; set; }
        public int PageCount { get; set; }
        public string Summary { get; set; }
        public int ChapterNumber { get; set; }
        public bool HasExercises { get; set; }
        public string KeyConcept { get; set; }
        public string DifficultyLevel { get; set; }
        public DateTime LastUpdated { get; set; }
    }
}
/*
var patientDtos = JsonSerializer.Deserialize<List<PatientDto>>(jsonString, options);

var patients = patientDtos.Select(dto => new Patient
{
    Id = dto.Id,
    FirstName = dto.FirstName,
    LastName = dto.LastName,
    AdmissionDate = DateOnly.FromDateTime(dto.AdmissionDate)
}).ToList();
*/

using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Cache;
using System.Text;
using System.Threading.Tasks;

namespace BookApplication.Domain.DomainModels
{
    public class Book : BaseEntity
    {
        public required string Title { get; set; }
        public required string ISBN { get; set; }
        public required string Description { get; set; }
        public required string Author { get; set; }
        public required int PublishedYear { get; set; }
    }
}
/*"id": 1,
    "name": "Book Title 1",
    "authorFirstName": "AuthorFirst1",
    "authorLastName": "AuthorLast1",
    "isbnCode": "978-3-16-148410-1",
    "shortDescription": "This is a description of book number 1.",
    "publishedYear": 2016,
    "rating": 1.2950411983945873,
    "genre": "Science",
    "pageCount": 120,
    "language": "German",
    "availabilityStatus": "Available"*/
