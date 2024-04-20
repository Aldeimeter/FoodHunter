// LanguageContext.js
import React, { createContext, useContext, useState, useEffect } from 'react';
import AsyncStorage from '@react-native-async-storage/async-storage';
import i18next from 'i18next';

const LanguageContext = createContext();

export const LanguageProvider = ({ children }) => {
  const [selectedLanguage, setSelectedLanguage] = useState('');

  useEffect(() => {
    const loadLanguage = async () => {
      try {
        const storedLanguage = await AsyncStorage.getItem('LanguagePreference');

        if (storedLanguage) {
          setSelectedLanguage(storedLanguage);
        
          console.log("Loaded language:", storedLanguage);
          i18next.changeLanguage(storedLanguage);
        }
      } catch (error) {
        console.error('Error loading language:', error);
      }
    };

    loadLanguage();
  }, []);

  const changeLanguage = async (languageValue) => {
    setSelectedLanguage(languageValue);

    i18next.changeLanguage(languageValue);

    try {
      await AsyncStorage.setItem('LanguagePreference', languageValue);

      console.log('Saved language:', languageValue);

    } catch (error) {
      console.error('Error saving language:', error);
    }
  };

  return (
    <LanguageContext.Provider value={{ selectedLanguage, changeLanguage }}>
      {children}
    </LanguageContext.Provider>
  );
};

export const useLanguage = () => useContext(LanguageContext);
