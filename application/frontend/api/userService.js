import { api, securedApi } from './api'; 

const registerUser = async (email, password) => {
    try {
        const response = await api.post('/auth/register', {
            email: email.toLowerCase(),
            password: password.trim(),
        });

        return response.data; // This returns the user data upon successful registration
    } catch (error) {
        throw new Error(error.response.headers['app-error'] || 'Failed to register user.');
    }
};

const login = async (username, password) => {
    const params = new URLSearchParams();
    params.append('username', username);
    params.append('password', password);

    try {
        const response = await api.post('/auth/login', params.toString(), {
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'  
            }
        });
        return response.data;  
    } catch (error) {
        throw new Error(error.response.headers['app-error'] || 'Login failed');
    }
};


const getMe = async () => {
  try {
    const response = await securedApi.get('/auth/me');
    return response.data;
  } catch (error) {
    throw new Error(error.response.headers['app-error'] || 'Failed to fetch user data.');
  }
};



const logoutUser = async () => {
  try {
    const response = await securedApi.post('/auth/logout');
    return response.data; 
  } catch (error) {
    if(error.response){
      throw new Error(error.response.headers['app-error']);
    }
    throw new Error('ERR_NETWORK');
  }
};

export { registerUser, login, getMe, logoutUser };
