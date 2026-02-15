import {Router,Routes, BrowserRouter, Route} from "react-router-dom"
import LoginPage from "../pages/login"
import DefaultLayout from "../layouts/Default_layout"
import { useContext } from "react"
import { UserContext, UserContextProvider } from "../context/Context"
import RoleBasedProtectedRoute from "../component/protectedRoute"
import NotFound from "../pages/notfound"
import Unauthorized from "../pages/unuthorized"
import UserProfile from "../component/profile"
import Homepage from "../pages/home"
import Dashboard from "../pages/DashboadPage"
import RegisterForm from "../pages/register"





function AppRouter () {
    
    return(
<UserContextProvider>
<BrowserRouter>
<Routes>
        <Route element={<DefaultLayout/>}>
            <Route path="/" element={
                <RoleBasedProtectedRoute allowedrole={["admin"]}>
                <Dashboard/>        
                </RoleBasedProtectedRoute>
                }/>

              <Route path="/register" element={
                <RoleBasedProtectedRoute allowedrole={["admin"]}>
                <RegisterForm/>              
                </RoleBasedProtectedRoute>
                }/>

                
        </Route>
        
        <Route path="/login" element={<LoginPage/>}/>
        
        <Route path="/notfound" element={<NotFound/>}/>
        <Route path="/unauthorized" element={<Unauthorized/>}/>
</Routes>
</BrowserRouter>
</UserContextProvider>
    )
}
export default AppRouter
