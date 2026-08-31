import React, { useState } from 'react';
import { Search, ChevronLeft, ChevronRight, Download } from 'lucide-react';

const DataTable = ({ columns, data, title, searchPlaceholder = "Search records..." }) => {
    const [searchTerm, setSearchTerm] = useState('');
    const [currentPage, setCurrentPage] = useState(1);
    const pageSize = 8;

    const filteredData = data.filter((item) => {
        if (!searchTerm) return true;
        return Object.values(item).some(val => 
            String(val).toLowerCase().includes(searchTerm.toLowerCase())
        );
    });

    const totalPages = Math.ceil(filteredData.length / pageSize) || 1;
    const paginatedData = filteredData.slice((currentPage - 1) * pageSize, currentPage * pageSize);

    const handleExportCSV = () => {
        if (data.length === 0) return;
        const headers = columns.map(c => c.header).join(',');
        const rows = filteredData.map(row => 
            columns.map(c => `"${row[c.accessor] || ''}"`).join(',')
        );
        const csvContent = "data:text/csv;charset=utf-8," + [headers, ...rows].join("\n");
        const encodedUri = encodeURI(csvContent);
        const link = document.createElement("a");
        link.setAttribute("href", encodedUri);
        link.setAttribute("download", `${title || 'export'}_data.csv`);
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    };

    return (
        <div className="bg-white rounded-3xl border border-slate-200 shadow-sm overflow-hidden space-y-4 p-6">
            <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
                <div>
                    <h3 className="text-base font-black text-slate-800">{title}</h3>
                    <p className="text-xs text-slate-400">Total {filteredData.length} records found</p>
                </div>
                <div className="flex items-center space-x-3">
                    <div className="relative">
                        <Search className="absolute left-3 top-2.5 h-4 w-4 text-slate-400" />
                        <input
                            type="text"
                            value={searchTerm}
                            onChange={(e) => { setSearchTerm(e.target.value); setCurrentPage(1); }}
                            placeholder={searchPlaceholder}
                            className="pl-9 pr-4 py-2 bg-slate-50 border border-slate-200 rounded-xl text-xs text-slate-800 focus:outline-none focus:ring-2 focus:ring-indigo-500"
                        />
                    </div>
                    <button
                        onClick={handleExportCSV}
                        className="px-3.5 py-2 bg-slate-100 hover:bg-slate-200 text-slate-700 rounded-xl text-xs font-bold flex items-center space-x-1.5 transition-all"
                    >
                        <Download className="h-3.5 w-3.5" />
                        <span>Export CSV</span>
                    </button>
                </div>
            </div>

            <div className="overflow-x-auto">
                <table className="w-full text-left text-xs">
                    <thead className="bg-slate-50 text-slate-500 uppercase tracking-wider font-black text-[10px] border-y border-slate-100">
                        <tr>
                            {columns.map((col, idx) => (
                                <th key={idx} className="py-3 px-4">{col.header}</th>
                            ))}
                        </tr>
                    </thead>
                    <tbody className="divide-y divide-slate-100 text-slate-700 font-medium">
                        {paginatedData.length === 0 ? (
                            <tr>
                                <td colSpan={columns.length} className="text-center py-8 text-slate-400">No matching records found.</td>
                            </tr>
                        ) : (
                            paginatedData.map((row, rIdx) => (
                                <tr key={rIdx} className="hover:bg-slate-50/70 transition-colors">
                                    {columns.map((col, cIdx) => (
                                        <td key={cIdx} className="py-3.5 px-4">
                                            {col.render ? col.render(row) : row[col.accessor]}
                                        </td>
                                    ))}
                                </tr>
                            ))
                        )}
                    </tbody>
                </table>
            </div>

            {/* Pagination Controls */}
            <div className="flex justify-between items-center pt-3 border-t border-slate-100 text-xs text-slate-500">
                <span>Page {currentPage} of {totalPages}</span>
                <div className="flex space-x-2">
                    <button
                        disabled={currentPage <= 1}
                        onClick={() => setCurrentPage(p => Math.max(1, p - 1))}
                        className="p-2 rounded-xl bg-slate-100 hover:bg-slate-200 disabled:opacity-40"
                    >
                        <ChevronLeft className="h-4 w-4" />
                    </button>
                    <button
                        disabled={currentPage >= totalPages}
                        onClick={() => setCurrentPage(p => Math.min(totalPages, p + 1))}
                        className="p-2 rounded-xl bg-slate-100 hover:bg-slate-200 disabled:opacity-40"
                    >
                        <ChevronRight className="h-4 w-4" />
                    </button>
                </div>
            </div>
        </div>
    );
};

export default DataTable;
