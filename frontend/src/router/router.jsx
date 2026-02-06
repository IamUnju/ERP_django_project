import { BrowserRouter,Routes,Route } from "react-router-dom";
import Login from "../pages/login";
import HomePage from "../pages/home";
import RegisterPage from "../pages/register";
import DefaultlayOut from "../layout/DefaultLayOut";
import UserContextProvider from "../context/Context";


function AppRouter (){
    return(
    <UserContextProvider>
    <BrowserRouter>
    <Routes>
        <Route element={<DefaultlayOut/>}>
        <Route path="/" element={<HomePage/>} />
        </Route>
        <Route path="/login" element={<Login/>}/>
        <Route path="/register" element={<RegisterPage/>}/>
    </Routes>
    </BrowserRouter>
  </UserContextProvider>

    )
}
export default AppRouter