// ThemeContext.js
import React, { createContext, useContext, useState, useEffect } from 'react';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { theme, darkTheme } from '../core/themes';

const ThemeContext = createContext();

export const ThemeProvider = ({ children }) => {
    const [currentTheme, setCurrentTheme] = useState(theme);

    useEffect(() => {
        const loadTheme = async () => {
          try {
            const storedTheme = await AsyncStorage.getItem('themePreference');

            console.log('Loaded theme:',storedTheme);

            if (storedTheme) {
              setCurrentTheme(storedTheme === "dark" ? darkTheme : theme);
            }
          } catch (error) {
            console.error('Error loading theme:', error);
          }
        }
        loadTheme();
    }, []);

    const toggleTheme = async () => {
        try {
          const newThemePreference = currentTheme.isDark ? "light" : "dark";

          setCurrentTheme(newThemePreference === "light" ? theme : darkTheme);

          await AsyncStorage.setItem('themePreference', newThemePreference);

          console.log('Stored theme:',newThemePreference);
        } catch (error) {
          console.log('Error saving theme:', error);
        }
    };

    return (
        <ThemeContext.Provider value={{ theme: currentTheme, toggleTheme }}>
            {children}
        </ThemeContext.Provider>
    );
};

export const useTheme = () => useContext(ThemeContext);
