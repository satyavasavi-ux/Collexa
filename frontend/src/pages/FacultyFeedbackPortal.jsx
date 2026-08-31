import React, { useState } from 'react';
import api from '../services/api';
import { Star, MessageSquare, CheckCircle2, Shield } from 'lucide-react';

const FacultyFeedbackPortal = () => {
    const [rating, setRating] = useState(5);
    const [comments, setComments] = useState('');
    const [submitted, setSubmitted] = useState(false);

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            await api.post('/api/student/feedback', {
                rating: rating,
                comments: comments
            });
            setSubmitted(true);
        } catch (err) {
            alert('Failed to submit appraisal');
        }
    };

    return (
        <div className="space-y-8 animate-fade-in max-w-xl mx-auto">
            <div className="text-center space-y-2">
                <div className="inline-flex p-3 rounded-2xl bg-indigo-50 text-indigo-600 mb-1">
                    <Shield className="h-6 w-6" />
                </div>
                <h1 className="text-2xl font-black text-slate-800">Anonymous Faculty & Course Appraisal</h1>
                <p className="text-xs text-slate-500">Your feedback is 100% anonymized and directly aids pedagogical improvements.</p>
            </div>

            {!submitted ? (
                <form onSubmit={handleSubmit} className="bg-white p-8 rounded-3xl border border-slate-200 shadow-sm space-y-6">
                    <div>
                        <label className="block text-xs font-bold text-slate-700 mb-3">Overall Satisfaction Rating</label>
                        <div className="flex space-x-2">
                            {[1, 2, 3, 4, 5].map((star) => (
                                <button
                                    key={star}
                                    type="button"
                                    onClick={() => setRating(star)}
                                    className={`p-3 rounded-2xl border transition-all ${
                                        rating >= star ? 'bg-amber-50 border-amber-300 text-amber-500' : 'bg-slate-50 border-slate-200 text-slate-300'
                                    }`}
                                >
                                    <Star className="h-6 w-6 fill-current" />
                                </button>
                            ))}
                        </div>
                    </div>

                    <div>
                        <label className="block text-xs font-bold text-slate-700 mb-1">Detailed Remarks / Suggestions</label>
                        <textarea
                            required
                            rows={4}
                            value={comments}
                            onChange={(e) => setComments(e.target.value)}
                            placeholder="Share your thoughts on lecture clarity, pacing, and practical assignments..."
                            className="w-full p-3.5 bg-slate-50 border border-slate-200 rounded-2xl text-xs text-slate-800 focus:ring-2 focus:ring-indigo-500 focus:outline-none"
                        />
                    </div>

                    <button
                        type="submit"
                        className="w-full py-3.5 bg-indigo-600 hover:bg-indigo-700 text-white text-xs font-bold rounded-2xl shadow-md transition-all"
                    >
                        Submit Confidential Feedback
                    </button>
                </form>
            ) : (
                <div className="bg-white p-8 rounded-3xl border border-slate-200 text-center space-y-3">
                    <CheckCircle2 className="h-10 w-10 text-emerald-600 mx-auto" />
                    <h3 className="text-lg font-black text-slate-800">Appraisal Recorded</h3>
                    <p className="text-xs text-slate-500">Thank you for helping us maintain top academic excellence.</p>
                </div>
            )}
        </div>
    );
};

export default FacultyFeedbackPortal;
