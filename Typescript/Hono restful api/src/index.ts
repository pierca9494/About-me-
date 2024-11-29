import { serve } from "@hono/node-server";
import { Hono } from "hono";

const app = new Hono();

app.get("/", (c) => {
  return c.text("Hello Hono!");
});

interface BookInterface {
  id: number | string;
  name: string;
  author: string;
}

const booksStorage: BookInterface[] = [];
const booksRouter = new Hono();

//get all the books
booksRouter.get("/", (c) => {
  return c.json(booksStorage);
});

//store the books
booksRouter.post("/", async (c) => {
  const book: BookInterface = await c.req.json();
  booksStorage.push(book);
  const response = {
    success: true,
    message: "Book added to storage successfully",
  };
  return c.json(response);
});

//update the books details
booksRouter.put("/:id", async (c) => {
  const bookId = parseInt(c.req.param("id"));

  const { name, author } = await c.req.json();
  const book = booksStorage.find((book) => book.id === bookId);

  if (!book) {
    const error = {
      success: false,
      message: "Book not found by the given Id",
    };
    return c.json(error, 404);
  }

  //update the book
  book.name = name;
  book.author = author;

  //update the storage
  // booksStorage[bookId] = book;

  const response = {
    success: true,
    message: "Book updated successfully",
  };
  return c.json(response);
});

booksRouter.get("/:id", async (c) => {
  const bookId = parseInt(c.req.param("id"));

  //find the book
  const book = booksStorage.find((book) => book.id === bookId);

  if (!book) {
    const error = {
      success: false,
      message: "Book not found by the given Id",
    };
    return c.json(error, 404);
  }

  const response = {
    success: true,
    message: "Book found successfully",
    data: book,
  };
  return c.json(response);
});

app.route("/api/books", booksRouter);

const port = 3000;
console.log(`Server is running on port http://localhost:${port}`);

serve({
  fetch: app.fetch,
  port,
});
