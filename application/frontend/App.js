// App.js
import React, { useState, useCallback, useEffect } from 'react';
import { NavigationContainer } from '@react-navigation/native';
import StackNavigator from './navigation/StackNavigator';
import { ThemeProvider } from "./core/ThemeContext";
import { LanguageProvider } from "./core/LanguageContext";
import LoadingScreen from './components/LoadingScreen';
import { useFonts } from 'expo-font';
import * as SplashScreen from 'expo-splash-screen';
import { View } from 'react-native';
import AsyncStorage from '@react-native-async-storage/async-storage';
import i18next from 'i18next';
import './lang/i18n.js';

SplashScreen.preventAutoHideAsync();

export default function App() {
  const [isLoaded] = useFonts({
    "merriweather-regular": require("./assets/fonts/Merriweather/Merriweather-Regular.ttf"),
    "merriweather-bold": require("./assets/fonts/Merriweather/Merriweather-Bold.ttf"),
  });
  const handleOnLayout = useCallback(async () => {
    console.log("Layout event triggered");
    if (isLoaded) {
      console.log("Fonts loaded, hiding splash screen");
      await SplashScreen.hideAsync();
    }
  }, [isLoaded]);

  if (!isLoaded){
    console.log("Fonts not loaded yet");
    return null;
  }

  return (
    <View onLayout={handleOnLayout} style={{ flex: 1 }}>
      <LanguageProvider>
        <ThemeProvider>
          <NavigationContainer>
           <StackNavigator/>
          </NavigationContainer>
        </ThemeProvider>
      </LanguageProvider>
    </View>
  );
}
