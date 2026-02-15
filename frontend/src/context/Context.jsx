import { createContext, useEffect, useState } from "react";
import {jwtDecode} from "jwt-decode";
import api from "../api";
import { ACCESS_TOKEN, REFRESH_TOKEN } from "../constant";

export const UserContext = createContext(null);

export const UserContextProvider = ({ children }) => {
    const [user, setUser] = useState(null);
    const [isAuthenticated, setIsAuthenticated] = useState(false);
    const [loading, setLoading] = useState(true);
    const [roles, setRoles] = useState([]);
    const [permissions, setPermissions] = useState([]);



    /*===============================
       get the profile data
    ================================*/

    const fetchProfile = async()=>{
        const response = await api.get('/api/profile/')
        // console.log("ime fike kweny profile")
        if (response.status === 200 && response.data){
            setUser({
                "user_id":response.data.user_id,
                "username":response.data.username,
                "role":response.data.role,
                "actions_permitted":{
                    "actoions": response.data.links
                }
            })
            setRoles(response.data.roles)
            setPermissions(response.data.links)
            setIsAuthenticated(true)
            // console.log(response.data.user_id)
            // console.log(response.data.username)
            // console.log(response.data.roles)    
        }

    }
     console.log({links:permissions})


    /* ===============================
       Refresh Access Token
    ================================ */
    const refreshAccessToken = async () => {
        try {
            const refreshToken = localStorage.getItem(REFRESH_TOKEN);
            if (!refreshToken){
                // console.log("token refresh empty")
                setIsAuthenticated(false)
                return false
            }     
            const response = await api.post("/api/refresh/", {refresh: refreshToken,});
            localStorage.setItem(ACCESS_TOKEN,response.data.access)

            if(response.data.refresh){
                localStorage.setItem(REFRESH_TOKEN,response.data.refresh)
            }
            return true
        } catch (error) {
            console.error("Refresh token failed", error);
            // logout();
            return null;
        }
    };

    /*===============================
       Check Authentication
    ================================ */

    const checkAuth = async () => {
        // console.log("imeta authentication")
        const token = localStorage.getItem(ACCESS_TOKEN)
        // console.log(token)
        if (!token){
            //  console.log("token empty")
            setLoading(false)

            return false
        }

        try{
            await fetchProfile()  
        }catch{
            const refreshToken = await refreshAccessToken()
            if(refreshToken){
                await fetchProfile()
            }
        }
        finally {
            setLoading(false)
        }  
    };

    /* ===============================
       Login
    ================================ */
    const Userlogin = async (username, password) => {
        try {
            const response = await api.post("/api/login/", {
                username,
                password,
            });
            
                // console.log(response.data.access)
                const { access, refresh } = response.data;
                localStorage.setItem(ACCESS_TOKEN, access);
                localStorage.setItem(REFRESH_TOKEN, refresh);
                setUser({user_id:response.data.user_id,username:response.data.username})
                setRoles(response.data.roles)
                setPermissions(response.data.links_permited)
                setIsAuthenticated(true);
                return { success: true };
                       
        } catch (error) {
            return {
                success: false,
                message: "Invalid credentials",
            };
        }
    };


    
                // if(isAuthenticated){
                //     console.log("auth ya ndani ya context")
                // }
    /* ===============================
       Logout
    ================================ */
    const logout = () => {
        localStorage.removeItem(ACCESS_TOKEN);
        localStorage.removeItem(REFRESH_TOKEN);
        setUser(null);
        setIsAuthenticated(false);
    };

    useEffect(() => {
        checkAuth();
    }, []);

    return (
        <UserContext.Provider
            value={{
                user,
                roles,
                permissions,
                isAuthenticated,
                loading,
                Userlogin,
                logout,
            }}
        >
            {children}
        </UserContext.Provider>
    );
};
