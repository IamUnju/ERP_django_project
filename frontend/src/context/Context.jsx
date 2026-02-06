import api from "../api";
import { useState,createContext, useContext } from "react";

const UserContext = createContext();
 
export const UserContextProvider = ({children})=>{
    const [user,setUser] = useState(null);
    const [loading,setLoading] = useState(false);
    const [error,setError] = useState(null);
    const [isAuthenticated,setIsAuthenticated] = useState(false);


    const fetch_user_profile = async () => {
        try{
            response = await api.get('')

        }catch(error)
        {

        }


    }


    const UserLogin = async (username,password) =>{
        try{
            const response = api.post('api/login/',{username,password})

        }catch(error){

        }
    }

    exportData = {
        UserLogin
    }
    return (<UserContext.Provider value={exportData}>{children}</UserContext.Provider>)
}

export const AuthContex = () => useContext(UserContext)