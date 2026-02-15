import React from "react";
import { Menu, Search, Bell, User, ChevronDown } from "lucide-react";

const Header = ({ onMenuClick }) => {
  return (
    <header className="header">
      <div className="header-left">
       
        
      </div>

      <div className="header-right">
        <div className="search-container">
          <Search className="search-icon" />
          <input type="text" placeholder="Search..." />
        </div>
        <Bell size={20} />
        <div className="user-info">
          <User size={20} />
          <span>Admin</span>
          <ChevronDown size={16} />
        </div>
      </div>
    </header>
  );
};

export default Header;