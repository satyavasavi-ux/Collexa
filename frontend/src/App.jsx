import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { AuthProvider } from './context/AuthContext';
import ProtectedRoute from './components/ProtectedRoute';
import MainLayout from './layouts/MainLayout';
import Login from './pages/Login';
import StudentDashboard from './pages/StudentDashboard';
import TeacherDashboard from './pages/TeacherDashboard';
import AdminDashboard from './pages/AdminDashboard';
import AdmissionPortal from './pages/AdmissionPortal';
import ExamCellPortal from './pages/ExamCellPortal';
import AccountPortal from './pages/AccountPortal';
import AttendanceScanner from './pages/AttendanceScanner';
import CourseLMSPortal from './pages/CourseLMSPortal';
import LibraryPortal from './pages/LibraryPortal';
import PlacementPortal from './pages/PlacementPortal';
import HostelTransportPortal from './pages/HostelTransportPortal';
import EventsClubsPortal from './pages/EventsClubsPortal';
import CommunityChat from './pages/CommunityChat';
import AIAssistantPortal from './pages/AIAssistantPortal';
import AnalyticsBI from './pages/AnalyticsBI';
import OnlineExamProctorPortal from './pages/OnlineExamProctorPortal';
import PayrollFinancePortal from './pages/PayrollFinancePortal';
import AssetInventoryPortal from './pages/AssetInventoryPortal';
import AlumniNetworkPortal from './pages/AlumniNetworkPortal';
import ScholarshipPortal from './pages/ScholarshipPortal';
import DigitalIdCardPortal from './pages/DigitalIdCardPortal';
import CertificateTranscriptPortal from './pages/CertificateTranscriptPortal';
import FacultyFeedbackPortal from './pages/FacultyFeedbackPortal';
import GrievanceRedressalPortal from './pages/GrievanceRedressalPortal';
import TimetableSchedulerPortal from './pages/TimetableSchedulerPortal';

const Unauthorized = () => (
  <div className="p-8 text-center bg-rose-50 min-h-screen flex items-center justify-center">
    <div className="bg-white p-8 rounded-3xl border border-rose-200 shadow-xl max-w-md">
      <h1 className="text-2xl font-black text-rose-600 uppercase tracking-tight">403 | Access Restricted</h1>
      <p className="text-xs text-slate-500 mt-2">You do not have administrative permission to view this institutional section.</p>
    </div>
  </div>
);

const App = () => {
  return (
    <Router>
      <AuthProvider>
        <Routes>
          <Route path="/login" element={<Login />} />

          <Route element={<ProtectedRoute><MainLayout /></ProtectedRoute>}>
            {/* Student Routes */}
            <Route path="/student" element={<ProtectedRoute allowedRoles={['STUDENT']}><StudentDashboard /></ProtectedRoute>} />
            <Route path="/student/scan" element={<ProtectedRoute allowedRoles={['STUDENT']}><AttendanceScanner /></ProtectedRoute>} />
            <Route path="/student/lms" element={<ProtectedRoute allowedRoles={['STUDENT']}><CourseLMSPortal /></ProtectedRoute>} />
            <Route path="/student/library" element={<ProtectedRoute allowedRoles={['STUDENT']}><LibraryPortal /></ProtectedRoute>} />
            <Route path="/student/placements" element={<ProtectedRoute allowedRoles={['STUDENT']}><PlacementPortal /></ProtectedRoute>} />
            <Route path="/student/hostel-transport" element={<ProtectedRoute allowedRoles={['STUDENT']}><HostelTransportPortal /></ProtectedRoute>} />
            <Route path="/student/events" element={<ProtectedRoute allowedRoles={['STUDENT']}><EventsClubsPortal /></ProtectedRoute>} />
            <Route path="/student/chat" element={<ProtectedRoute allowedRoles={['STUDENT']}><CommunityChat /></ProtectedRoute>} />
            <Route path="/student/ai-tutor" element={<ProtectedRoute allowedRoles={['STUDENT']}><AIAssistantPortal /></ProtectedRoute>} />
            <Route path="/student/exam-proctor" element={<ProtectedRoute allowedRoles={['STUDENT']}><OnlineExamProctorPortal /></ProtectedRoute>} />
            <Route path="/student/id-card" element={<ProtectedRoute allowedRoles={['STUDENT']}><DigitalIdCardPortal /></ProtectedRoute>} />
            <Route path="/student/certificates" element={<ProtectedRoute allowedRoles={['STUDENT']}><CertificateTranscriptPortal /></ProtectedRoute>} />
            <Route path="/student/feedback" element={<ProtectedRoute allowedRoles={['STUDENT']}><FacultyFeedbackPortal /></ProtectedRoute>} />
            <Route path="/student/grievances" element={<ProtectedRoute allowedRoles={['STUDENT']}><GrievanceRedressalPortal /></ProtectedRoute>} />
            <Route path="/student/scholarships" element={<ProtectedRoute allowedRoles={['STUDENT']}><ScholarshipPortal /></ProtectedRoute>} />

            {/* Teacher Routes */}
            <Route path="/teacher" element={<ProtectedRoute allowedRoles={['TEACHER']}><TeacherDashboard /></ProtectedRoute>} />
            <Route path="/teacher/lms" element={<ProtectedRoute allowedRoles={['TEACHER', 'ADMIN']}><CourseLMSPortal /></ProtectedRoute>} />

            {/* Super Admin & Analytics */}
            <Route path="/admin" element={<ProtectedRoute allowedRoles={['ADMIN']}><AdminDashboard /></ProtectedRoute>} />
            <Route path="/admin/analytics" element={<ProtectedRoute allowedRoles={['ADMIN', 'EXAM', 'ACCOUNT']}><AnalyticsBI /></ProtectedRoute>} />
            <Route path="/admin/lms" element={<ProtectedRoute allowedRoles={['ADMIN']}><CourseLMSPortal /></ProtectedRoute>} />

            {/* Department Portals */}
            <Route path="/admission" element={<ProtectedRoute allowedRoles={['ADMISSION', 'ADMIN']}><AdmissionPortal /></ProtectedRoute>} />
            <Route path="/exam-cell" element={<ProtectedRoute allowedRoles={['EXAM', 'ADMIN']}><ExamCellPortal /></ProtectedRoute>} />
            <Route path="/account-section" element={<ProtectedRoute allowedRoles={['ACCOUNT', 'ADMIN']}><AccountPortal /></ProtectedRoute>} />
            <Route path="/library" element={<ProtectedRoute allowedRoles={['LIBRARY', 'ADMIN', 'TEACHER']}><LibraryPortal /></ProtectedRoute>} />
            <Route path="/placements" element={<ProtectedRoute allowedRoles={['PLACEMENT', 'ADMIN']}><PlacementPortal /></ProtectedRoute>} />
            <Route path="/hostel-transport" element={<ProtectedRoute allowedRoles={['HOSTEL', 'TRANSPORT', 'ADMIN']}><HostelTransportPortal /></ProtectedRoute>} />
            <Route path="/events" element={<ProtectedRoute allowedRoles={['ADMIN', 'TEACHER']}><EventsClubsPortal /></ProtectedRoute>} />
            <Route path="/payroll" element={<ProtectedRoute allowedRoles={['ACCOUNT', 'ADMIN', 'TEACHER']}><PayrollFinancePortal /></ProtectedRoute>} />
            <Route path="/inventory" element={<ProtectedRoute allowedRoles={['ADMIN', 'ACCOUNT']}><AssetInventoryPortal /></ProtectedRoute>} />
            <Route path="/alumni" element={<ProtectedRoute><AlumniNetworkPortal /></ProtectedRoute>} />
            <Route path="/scholarships" element={<ProtectedRoute><ScholarshipPortal /></ProtectedRoute>} />
            <Route path="/timetable-scheduler" element={<ProtectedRoute><TimetableSchedulerPortal /></ProtectedRoute>} />
            <Route path="/chat" element={<ProtectedRoute><CommunityChat /></ProtectedRoute>} />
            <Route path="/ai-assistant" element={<ProtectedRoute><AIAssistantPortal /></ProtectedRoute>} />
          </Route>

          <Route path="/unauthorized" element={<Unauthorized />} />
          <Route path="*" element={<Navigate to="/" replace />} />
          <Route path="/" element={<Navigate to="/login" replace />} />
        </Routes>
      </AuthProvider>
    </Router>
  );
};

export default App;
