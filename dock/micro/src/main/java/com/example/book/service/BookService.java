package com.example.book.service;
import com.example.book.model.*;
import com.example.book.repository.BookRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class BookService {
    @Autowired
    private BookRepository bookRepository;

    public List<Book> getAllBooks() {

        return bookRepository.findAll();

    }

    public Book getBookById(Long id) {
        return bookRepository.findById(id).orElse(null);
    }
}
