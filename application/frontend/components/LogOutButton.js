// components/LogoutButton.js
import React, { useState } from 'react';
import { TouchableOpacity, Text, StyleSheet, View } from 'react-native';
// Language stuff
import { useTranslation } from 'react-i18next';
// Theme stuff
import { useTheme } from '../core/ThemeContext';
// Auth stuff
import { useAuth } from '../core/AuthContext';
// userService import 
import { logoutUser } from '../api/userService';
// Loading scene stuff 
import { useLoading } from '../core/LoadingContext';

const LogOutButton = () => {
  const { removeTokens } = useAuth();
  const { theme } = useTheme();

  const styles = createStyles(theme);

  const {t} = useTranslation();
  
  const [message, setMessage] = useState(null);

  const { showLoading, hideLoading } = useLoading();

  const handleLogout = async () => {
      try {
          showLoading();
          await logoutUser();
          await removeTokens();
          hideLoading();
      } catch (error) {
          console.error(error.message);  
          setMessage(t(error.message));
          if(error.message !== "ERR_NETWORK"){
            await removeTokens();
          }
          hideLoading();
      }
  };
   
  return (
    <View>
      <TouchableOpacity style={styles.button} onPress={handleLogout}>
          <Text style={styles.text}>{t('LOGOUT')}</Text>
      </TouchableOpacity>
      {message && <Text style={[styles.text, {color: theme.colors.danger}]}>{message}</Text>}
    </View>
  );
};

const createStyles = (theme) => StyleSheet.create({
    button: {
        backgroundColor: theme.colors.danger, 
        padding: 10,
        borderRadius: 5,
        alignItems: 'center',
        justifyContent: 'center',
        marginTop: 10,
    },
    text: {
        color: '#fff',  // White text for contrast, change as needed
        fontSize: 16
    }
});

export default LogOutButton;
