// App.js
// React stuff
import React, { useState, useCallback } from 'react';
import { View, SafeAreaView } from 'react-native';
// Navigation 
import { NavigationContainer } from '@react-navigation/native';
import AuthStackNavigator from './navigation/AuthStackNavigator';
import MainStackNavigator from './navigation/MainStackNavigator';
// Preferences persistence
import { ThemeProvider } from "./core/ThemeContext";
import { LanguageProvider } from "./core/LanguageContext";
// Fonts
import { FontsProvider } from './core/FontsContext'; 
// Localization stuff
import './lang/i18n.js';
// Authentication stuff 
import { AuthProvider, useAuth } from "./core/AuthContext";
// Loading scene stuff 
import { LoadingProvider, useLoading } from './core/LoadingContext';
import LoadingScreen from './components/LoadingScreen';


const AppContent = () => {
  const { isAuthenticated } = useAuth();
  const { isLoading } = useLoading();

  return (
    <SafeAreaView style={{ flex: 1 }}>
      <NavigationContainer>
        {isAuthenticated ? <MainStackNavigator/> : <AuthStackNavigator/>}
        {isLoading && <LoadingScreen/>}
      </NavigationContainer>
    </SafeAreaView>
  );
}

export default function App() {
  return (
    <LoadingProvider>
      <AuthProvider>   
        <FontsProvider>
          <LanguageProvider>
            <ThemeProvider>
              <AppContent/>
            </ThemeProvider>
          </LanguageProvider>
        </FontsProvider>
      </AuthProvider>   
    </LoadingProvider>
  )
}
