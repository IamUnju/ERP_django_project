import { useContext,useState } from "react"
import { UserContext } from "../context/Context"
import { useNavigate} from "react-router-dom"

function Form () {
    const {Userlogin}=useContext(UserContext)
    const[username,setUsername]=useState("")
    const[password,setPassword]=useState("")
    const navigate = useNavigate()

const handlesubmission = async (e)=>{
    e.preventDefault()

    const login = await Userlogin(username,password);
    if(login){
        // console.log("from the login")
        navigate("/",{replace:true})
    }


}


    return(
        <div>
            <form onSubmit={handlesubmission}>
                <input type="text" placeholder="username" value={username} onChange={(e)=>setUsername(e.target.value)} />
                <input type="password" placeholder="password" value={password} onChange={(e)=>setPassword(e.target.value)} />
            <button type="submit">Login</button>

            </form>
        </div>
    
    )
}
export default Form