import React, { useEffect, useRef, useState } from "react";
import api from "../api";

const RegisterForm = () =>{
    const [username,setUsername] = useState("")
    const [email,setEmail] = useState("")
    const [password,setPassword]= useState("")


     const [Depts,setDepts] = useState([])
     const [Deptid,setDept_id] = useState("")
     const [Userstatus, setUserStatus]=useState("ACTIVE")
    //  console.log(Userstatus)

    const loadDepartment =  async () =>{
        const loadedData = await api.get('/api/list/departiment/')
        if(loadedData){
            setDepts(loadedData.data)
        }
    }
    const formSubmit =  async (e)=>{
        e.preventDefault()
        const DataPayload = {
            username : username,
            email : email,
            password : password,
            department : Deptid,
            userstatus : Userstatus
        }

        // console.log("submiited successful",DataPayload)
        try
        {
            const res = await api.post("/api/register/",DataPayload)
            if(res){
                // console.log(res.data)
                alert("data save successifuly")
            }
        }
        catch(error){
            console.log(error)
        }
        

    } 
    useEffect(()=>{
        loadDepartment()
    },[])

    return (
        <div className="container">
            <div className="form-container">
                <form onSubmit={formSubmit}> 
                    <div className="input-field">
                        <label>Username</label>
                        <input value={username} onChange={(e)=>{setUsername(e.target.value)}} type="text" placeholder="enter username" />
                    </div>
                    <div className="input-field">
                        <label>Email</label>
                        <input value={email} onChange={e=>setEmail(e.target.value)} type="email" placeholder="enter email" />
                    </div>
                    <div className="input-field">
                        <label>password</label>
                        <input value={password} onChange={e=>setPassword(e.target.value)} type="password" placeholder="enter password" />
                    </div>
                    <div className="input-field">
                        <label>choose department</label>
                        <select value={Deptid} onChange={(e)=>{setDept_id(e.target.value)}}>
                            <option value="">choose Department </option>
                            {Depts.map(Dept=>(
                                <option key={Dept.dept_id} value={Dept.dept_id}>
                                    {Dept.departiment}
                                </option>))}    
                        </select>
                    </div>
                    <div className="input-field">
                        <label>User Status</label>
                        <select value={Userstatus} onChange={e=>setUserStatus(e.target.value)}>
                            <option value={'ACTIVE'}>ACTIVE</option>
                            <option value={'INACTIVE'}>INACTIVE</option>
                        </select>
                    </div>
                    <div className="input-field">
                        <button type="submit">Save</button>
                    </div>

                </form>

            </div>

        </div>
        
    )



}
export default RegisterForm