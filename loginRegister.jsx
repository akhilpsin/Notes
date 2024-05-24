import React, { useState, useEffect } from "react";  
import axios from 'axios';  
import "./LoginSignup.css";  
import user_icon from "../Assets/person.png";  
import email_icon from "../Assets/email.png";  
import password_icon from "../Assets/password.png";  
  
axios.defaults.xsrfCookieName = 'csrftoken';  
axios.defaults.xsrfHeaderName = 'X-CSRFToken';  
axios.defaults.withCredentials = true;  
  
const client = axios.create({  
  baseURL: "http://127.0.0.1:8000"  
});  
  
const LoginSignup = () => {  
  const [action, setAction] = useState("Sign Up");  
  const [currentUser, setCurrentUser] = useState();  
  const [email, setEmail] = useState('');  
  const [username, setUsername] = useState('');  
  const [password, setPassword] = useState('');  
  
  function submitRegistration(e) {  
    e.preventDefault();  
    client.post(  
      "/api/register",  
      {  
        email: email,  
        username: username,  
        password: password  
      }  
    ).then(function(res) {  
      client.post(  
        "/api/login",  
        {  
          email: email,  
          password: password  
        }  
      ).then(function(res) {  
        setCurrentUser(true);  
      }).catch(function(error) {  
        console.error("Login error:", error);  
        alert("Login failed. Please check your credentials and try again.");  
      });  
    }).catch(function(error) {  
      console.error("Registration error:", error);  
      alert("Registration failed. Please check your details and try again.");  
    });  
  }  
  
  function submitLogin(e) {  
    e.preventDefault();  
    client.post(  
      "/api/login",  
      {  
        email: email,  
        password: password  
      }  
    ).then(function(res) {  
      setCurrentUser(true);  
    }).catch(function(error) {  
      console.error("Login error:", error);  
      alert("Login failed. Please check your credentials and try again.");  
    });  
  }  
  
  function submitLogout(e) {  
    e.preventDefault();  
    client.post(  
      "/api/logout",  
      { withCredentials: true }  
    ).then(function(res) {  
      setCurrentUser(false);  
    }).catch(function(error) {  
      console.error("Logout error:", error);  
      alert("Logout failed. Please try again.");  
    });  
  }  
  
  if (currentUser) {  
    return (  
      <div className="container">  
        <div className="submit-container">  
          <div className="submit" onClick={e => submitLogout(e)}>Log out</div>  
          <div>  
            <h2>You're logged in!</h2>  
          </div>  
        </div>  
      </div>  
    );  
  }  
  
  return (  
    <div className="container">  
      <div className="submit-container">  
        <div className={action === "Sign Up" ? "submit gray" : "submit"} onClick={() => { setAction("Login"); }}>  
          Login  
        </div>  
        <div className={action === "Login" ? "submit gray" : "submit"} onClick={() => { setAction("Sign Up"); }}>  
          Sign Up  
        </div>  
      </div>  
      <div className="header">  
        <div className="text"> {action}</div>  
        <div className="underline"></div>  
      </div>  
      <div className="inputs">  
        {action === "Login" ? (  
          <div></div>  
        ) : (  
          <div className="input">  
            <img src={user_icon} alt="" />  
            <input type="text" placeholder="Name" value={username} onChange={e => setUsername(e.target.value)} />  
          </div>  
        )}  
        <div className="input">  
          <img src={email_icon} alt="" />  
          <input type="email" placeholder="Email" value={email} onChange={e => setEmail(e.target.value)} />  
        </div>  
        <div className="input">  
          <img src={password_icon} alt="" />  
          <input type="password" placeholder="Password" value={password} onChange={e => setPassword(e.target.value)} />  
        </div>  
      </div>  
      {action === "Login" ? (  
        <div className="forgot-password">  
          Lost Password? <span>Click here!</span>  
        </div>  
      ) : (  
        <div></div>  
      )}  
      {action === "Login" ? (  
        <div className="submit_api" onClick={e => submitLogin(e)}> Login </div>  
      ) : (  
        <div className="submit_api" onClick={e => submitRegistration(e)}> Register </div>  
      )}  
    </div>  
  );  
};  
  
export default LoginSignup;  
