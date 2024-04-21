// core/AuthContext.js
// base_url 
import { base_url } from './config';
// encrypted storage 
import { save, get, remove } from './userDataStorage';
// userService import 
import { refreshAccessToken } from '../api/api';
import React, { createContext, useState, useContext, useEffect } from 'react';

const AuthContext = createContext();

export const useAuth = () => useContext(AuthContext);

export const AuthProvider = ({ children }) => {
    const [isAuthenticated, setIsAuthenticated] = useState(false);
    const [isServerReachable, setIsServerReachable] = useState(false);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        checkAuthStatus();
        const interval = setInterval(() => {
            checkTokenExistence();
        }, 60000 * 5);  // Check every 5 minutes

        return () => clearInterval(interval);  // Clear interval on component unmount
    }, []);

    const checkAuthStatus = async () => {
        try {
            const token = await get('access_token');
            setIsAuthenticated(!!token);
            await checkServerHealth();
            console.log("User is authenticated:", !!token);
            if(!!token && isServerReachable){
              try {
                console.log("Refreshing token")
                const accessToken = await refreshAccessToken();
                if(accessToken){
                  save('access_token', accessToken);
                }
              } catch (error) {
                console.error(error);
              }
            }
            setLoading(false);
        } catch (error) {
            setIsAuthenticated(false);
            setLoading(false);
        }
    };

    const checkServerHealth = async () => {
        try {
            const response = await fetch(base_url + '/health');
            setIsServerReachable(response.ok);
            console.log("Server is reachable:", response.ok);
        } catch (error) {
            console.error('Backend not reachable:', error);
            setIsServerReachable(false);
        }
    };

    const setTokens = async (access_token, refresh_token) => { 
        await save('access_token', access_token);
        await save('refresh_token', refresh_token);
        setIsAuthenticated(true);
        console.log("Logged in");
    };

    const removeTokens = async () => {
        await remove('access_token');
        await remove('refresh_token');
        setIsAuthenticated(false);
        console.log("Logged out");
    };

    const checkTokenExistence = async () => {
        const accessToken = await get('access_token');
        if (!accessToken) {
            setIsAuthenticated(false);
        }
    };

    return (
        <AuthContext.Provider value={{
            isAuthenticated,
            setTokens,
            removeTokens,
            loading
        }}>
            {children}
        </AuthContext.Provider>
    );
};

export default AuthProvider;
