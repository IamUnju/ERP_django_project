import React, { useState, useRef, useEffect } from "react";
import { User, ChevronDown } from "lucide-react";

const UserProfile = () => {
  const [open, setOpen] = useState(false);
  const menuRef = useRef();

  // Close dropdown when clicking outside
  useEffect(() => {
    const handleClickOutside = (event) => {
      if (menuRef.current && !menuRef.current.contains(event.target)) {
        setOpen(false);
      }
    };
    document.addEventListener("mousedown", handleClickOutside);
    return () => document.removeEventListener("mousedown", handleClickOutside);
  }, []);

  return (
    <div className="user-menu" ref={menuRef}>
      <button
        onClick={() => setOpen(!open)}
        className="flex items-center gap-1 p-2 hover:bg-gray-100 rounded"
      >
        <User className="w-5 h-5" /> Admin <ChevronDown className="w-4 h-4" />
      </button>

      {open && (
        <div className="dropdown">
          <ul>
            <li><button>Profile</button></li>
            <li><button>Settings</button></li>
            <li><button>Logout</button></li>
          </ul>
        </div>
      )}
    </div>
  );
};

export default UserProfile;
