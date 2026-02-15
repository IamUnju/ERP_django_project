import React from "react";
import { Home, User, Settings, LogOut } from "lucide-react";

const Sidebar = ({ isOpen, toggleSidebar,onMenuClick }) => {
  return (
    <aside className={`sidebar ${isOpen ? "open" : "closed"}`}>
      {/* Optional: Add a toggle button inside sidebar for closed state */}
      {/* <button className="toggle-btn" onClick={toggleSidebar}>
        {isOpen ? "←" : "→"}
      </button> */}
      <div className="sidebar-header">
  <div className="header-logo" onClick={onMenuClick}>S</div>



  {isOpen && <span style={{fontWeight: "600"}}>System</span>}
</div>

      <nav className="sidebar-nav">
        <ul className="menu-items">
          <li>
            <Home size={20} />
            {isOpen && <span>Home Page</span>}
          </li>
          <li>
            <User size={20} />
            {isOpen && <span>Profile</span>}
          </li>
          <li>
            <Settings size={20} />
            {isOpen && <span>Settings</span>}
          </li>
          <li>
            <LogOut size={20} />
            {isOpen && <span>Logout</span>}
          </li>
        </ul>
      </nav>
    </aside>
  );
};

export default Sidebar;