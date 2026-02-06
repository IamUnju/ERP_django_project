import axios from 'axios';
import { REFRESH_TOKEN,ACCESS_TOKEN,MAIN_URL } from './constant';

const api = axios.create({
    baseURL:MAIN_URL,
    headers :{
        'Content-Type':'application/json'
    }
})

api.interceptors.request.use(
    (config)=>{
        const token = localStorage.getItem(ACCESS_TOKEN)
        if(token){
            config.headers.Authorization = `Bearer ${token}`
        }
        return config
    },
    
    (error)=>{
        return Promise.reject(error)
    }
)

api
export default api;