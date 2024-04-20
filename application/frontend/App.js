// App.js
// React stuff
import React, { useState, useCallback } from 'react';
import { View, SafeAreaView } from 'react-native';
// Navigation 
import { NavigationContainer } from '@react-navigation/native';
import StackNavigator from './navigation/StackNavigator';
// Preferences persistence
import { ThemeProvider } from "./core/ThemeContext";
import { LanguageProvider } from "./core/LanguageContext";
// Fonts
import { FontsProvider } from './core/FontsContext'; 
// Localization stuff
import './lang/i18n.js';


export default function App() {
  return (
    <SafeAreaView style={{ flex: 1 }}>
      <FontsProvider>
        <LanguageProvider>
          <ThemeProvider>
            <NavigationContainer>
             <StackNavigator/>
            </NavigationContainer>
          </ThemeProvider>
        </LanguageProvider>
      </FontsProvider>
    </SafeAreaView>
  );
}
