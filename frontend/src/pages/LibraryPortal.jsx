import React, { useState, useEffect } from 'react';
import api from '../services/api';
import { useAuth } from '../context/AuthContext';
import { Book, Search, BookmarkCheck, Clock, CheckCircle2, AlertCircle, Plus, Filter, Tag, RotateCcw } from 'lucide-react';

const LibraryPortal = () => {
    const { user } = useAuth();
    const [books, setBooks] = useState([]);
    const [borrows, setBorrows] = useState([]);
    const [searchTerm, setSearchTerm] = useState('');
    const [selectedCategory, setSelectedCategory] = useState('All');
    const [loading, setLoading] = useState(true);
    const [actionMsg, setActionMsg] = useState('');

    useEffect(() => {
        fetchLibraryData();
    }, [searchTerm, selectedCategory]);

    const fetchLibraryData = async () => {
        setLoading(true);
        try {
            let url = '/api/library/books';
            const params = [];
            if (searchTerm) params.push(`search=${encodeURIComponent(searchTerm)}`);
            if (selectedCategory !== 'All') params.push(`category=${encodeURIComponent(selectedCategory)}`);
            if (params.length > 0) url += `?${params.join('&')}`;

            const [booksRes, borrowsRes] = await Promise.all([
                api.get(url),
                api.get('/api/library/borrows/active')
            ]);
            setBooks(booksRes.data);
            setBorrows(borrowsRes.data);
        } catch (err) {
            console.error('Failed to load library catalog', err);
        } finally {
            setLoading(false);
        }
    };

    const handleIssueBook = async (bookId) => {
        try {
            await api.post('/api/library/issue', {
                book_id: bookId,
                user_id: user?.id,
                borrow_date: new Date().toISOString().split('T')[0]
            });
            setActionMsg('Book successfully checked out! Return within 14 days.');
            setTimeout(() => setActionMsg(''), 4000);
            fetchLibraryData();
        } catch (err) {
            alert(err.response?.data?.detail || 'Failed to issue book');
        }
    };

    const handleReturnBook = async (borrowId) => {
        try {
            await api.post(`/api/library/return/${borrowId}`);
            setActionMsg('Book returned successfully to library catalog.');
            setTimeout(() => setActionMsg(''), 4000);
            fetchLibraryData();
        } catch (err) {
            alert('Failed to return book');
        }
    };

    const categories = ['All', 'Computer Science', 'Software Engineering', 'Software Architecture', 'Electronics', 'Mathematics'];

    return (
        <div className="space-y-8 animate-fade-in">
            {/* Header */}
            <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 bg-gradient-to-r from-emerald-900 via-teal-900 to-slate-900 p-8 rounded-3xl text-white shadow-xl">
                <div>
                    <div className="inline-flex items-center space-x-2 px-3 py-1 rounded-full bg-emerald-500/20 text-emerald-300 text-xs font-bold uppercase tracking-wider mb-3">
                        <Book className="h-3.5 w-3.5" />
                        <span>Central Digital Library</span>
                    </div>
                    <h1 className="text-3xl font-black tracking-tight">Library Catalog & Book Circulation</h1>
                    <p className="text-slate-300 text-sm mt-1">Search through 25,000+ textbook titles, research papers, and manage borrowed books.</p>
                </div>
            </div>

            {actionMsg && (
                <div className="p-4 rounded-2xl bg-emerald-50 border border-emerald-200 text-emerald-800 text-sm font-bold flex items-center shadow-sm">
                    <CheckCircle2 className="h-4 w-4 mr-2 text-emerald-600" />
                    {actionMsg}
                </div>
            )}

            {/* Active Borrows Banner for Student */}
            {borrows.length > 0 && (
                <div className="bg-amber-500/10 border border-amber-500/30 rounded-3xl p-6 space-y-3">
                    <h3 className="text-xs font-black uppercase tracking-widest text-amber-700 flex items-center">
                        <Clock className="h-4 w-4 mr-1.5" />
                        Currently Issued Books ({borrows.length})
                    </h3>
                    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                        {borrows.map((b) => (
                            <div key={b.id} className="bg-white p-4 rounded-2xl border border-amber-200 shadow-sm flex justify-between items-center">
                                <div>
                                    <h4 className="text-xs font-bold text-slate-800">{b.book?.title || `Book ID #${b.book_id}`}</h4>
                                    <p className="text-[10px] text-slate-500 mt-1">Due: <span className="font-bold text-amber-600">{b.due_date}</span></p>
                                </div>
                                <button
                                    onClick={() => handleReturnBook(b.id)}
                                    className="px-3 py-1.5 bg-slate-800 hover:bg-slate-700 text-white text-[10px] font-black uppercase tracking-wider rounded-xl shadow-sm"
                                >
                                    Return
                                </button>
                            </div>
                        ))}
                    </div>
                </div>
            )}

            {/* Search & Category Filter Bar */}
            <div className="flex flex-col sm:flex-row gap-4 justify-between items-center bg-white p-4 rounded-2xl border border-slate-200 shadow-sm">
                <div className="relative w-full sm:w-96">
                    <Search className="absolute left-3.5 top-3 h-4 w-4 text-slate-400" />
                    <input
                        type="text"
                        value={searchTerm}
                        onChange={(e) => setSearchTerm(e.target.value)}
                        placeholder="Search by Title, Author, or ISBN..."
                        className="w-full pl-10 pr-4 py-2 bg-slate-50 border border-slate-200 rounded-xl text-xs text-slate-800 focus:outline-none focus:ring-2 focus:ring-emerald-500"
                    />
                </div>
                <div className="flex overflow-x-auto space-x-2 w-full sm:w-auto pb-1 sm:pb-0">
                    {categories.map((cat) => (
                        <button
                            key={cat}
                            onClick={() => setSelectedCategory(cat)}
                            className={`px-3.5 py-1.5 rounded-xl text-xs font-bold whitespace-nowrap transition-all ${
                                selectedCategory === cat
                                    ? 'bg-emerald-600 text-white shadow-sm'
                                    : 'bg-slate-100 text-slate-600 hover:bg-slate-200'
                            }`}
                        >
                            {cat}
                        </button>
                    ))}
                </div>
            </div>

            {/* Books Grid */}
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
                {books.map((book) => (
                    <div key={book.id} className="bg-white rounded-3xl p-5 border border-slate-200 shadow-sm flex flex-col justify-between hover:shadow-md transition-all">
                        <div className="space-y-3">
                            <div className="h-40 rounded-2xl bg-gradient-to-br from-slate-100 to-slate-200 border border-slate-200/80 flex items-center justify-center p-4 text-center">
                                <div>
                                    <Book className="h-8 w-8 mx-auto text-emerald-600 mb-2 opacity-70" />
                                    <p className="text-xs font-black text-slate-800 line-clamp-2">{book.title}</p>
                                    <p className="text-[10px] text-slate-500 mt-1">{book.author}</p>
                                </div>
                            </div>
                            <div>
                                <span className="text-[10px] font-bold px-2 py-0.5 rounded-md bg-emerald-50 text-emerald-700 border border-emerald-200">
                                    {book.category}
                                </span>
                                <h3 className="text-sm font-bold text-slate-800 mt-2 line-clamp-1">{book.title}</h3>
                                <p className="text-xs text-slate-500">{book.author} • {book.publisher}</p>
                                <div className="text-[10px] text-slate-400 mt-2 flex justify-between">
                                    <span>ISBN: {book.isbn}</span>
                                    <span>Rack: {book.rack_location}</span>
                                </div>
                            </div>
                        </div>

                        <div className="mt-4 pt-4 border-t border-slate-100 flex items-center justify-between">
                            <span className={`text-xs font-bold ${book.available_copies > 0 ? 'text-emerald-600' : 'text-rose-500'}`}>
                                {book.available_copies > 0 ? `${book.available_copies} Available` : 'Out of Stock'}
                            </span>
                            <button
                                disabled={book.available_copies <= 0}
                                onClick={() => handleIssueBook(book.id)}
                                className="px-4 py-2 bg-emerald-600 hover:bg-emerald-700 disabled:opacity-40 text-white text-xs font-bold rounded-xl shadow-sm transition-all"
                            >
                                Issue Book
                            </button>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default LibraryPortal;
