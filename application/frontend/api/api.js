import axios from 'axios';
import { get, save, remove } from '../core/userDataStorage';

const api = axios.create({
  baseURL: 'http://192.168.100.44:8000',
    headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json', 
    }
});


const refreshAccessToken = async () => {
  try {
    console.log('Trying to retrieve refresh token from storage');
    const refreshToken = await get('refresh_token');
    if (refreshToken) {
      console.log('Refreshing access token');
      const response = await api.get('/auth/refresh', {
        params: {
          refresh_token: refreshToken,
        },
      });
      if (response.status === 200) {
        console.log('Access token was refreshed');
        return response.data.access_token; 
      } else {
        throw new Error('Failed to refresh access token');
      }
    } else {
      throw new Error('Refresh token not found');
    }
  } catch (error) {
    console.error('Error refreshing access token:', error);
    remove('refresh_token');
    remove('access_token');
    throw error; // Propagate the error if needed
  }
};

const securedApi = axios.create({
  baseURL: 'http://192.168.100.44:8000',
    headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }
});

securedApi.interceptors.request.use(
  async (config) => {
    console.log('Trying to retrive access token');
    const accessToken = await get('access_token');
    if (accessToken) {
      console.log('Access Token is inserted to request header');
      config.headers.Authorization = `Bearer ${accessToken}`;
    }
    return config;
  },
  (error) => {
    console.error(error);
    Promise.reject(error);
  }
);

securedApi.interceptors.response.use(
  (response) => {
    return response;
  },
  async (error) => {
    console.error('Error while accessing secured endpoint:', error.message);
    if(error.code === 'ERR_NETWORK'){
      throw new Error(error.code);
    }
    const originalRequest = error.config;
    if (error.response && error.response.status === 403 && !originalRequest._retry) {
      console.log('Trying to refresh access token');
      originalRequest._retry = true;
      const newAccessToken = await refreshAccessToken(); 
      if (newAccessToken) {
        console.log('New access token was received');
        console.log('Saving new access token');
        save('access_token', newAccessToken); 
        originalRequest.headers.Authorization = `Bearer ${newAccessToken}`;
        console.log('Resending original request');
        return securedApi(originalRequest);
      }
    }
    return Promise.reject(error);
  }
);
export { api, securedApi, refreshAccessToken };
