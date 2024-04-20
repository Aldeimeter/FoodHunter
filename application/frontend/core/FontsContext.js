import React, { createContext, useContext, useEffect, useState } from 'react';
import * as SplashScreen from 'expo-splash-screen';
import { useFonts } from 'expo-font';

const FontsContext = createContext();

export const useFontsProvider = () => useContext(FontsContext);

export const FontsProvider = ({ children }) => {
  const [fontsLoaded] = useFonts({
    "merriweather-regular": require("../assets/fonts/Merriweather/Merriweather-Regular.ttf"),
    "merriweather-bold": require("../assets/fonts/Merriweather/Merriweather-Bold.ttf"),
  });

  useEffect(() => {
    async function prepare() {
      try {
        await SplashScreen.preventAutoHideAsync();
        if (fontsLoaded) {
          await SplashScreen.hideAsync();
        }
      } catch (e) {
        console.warn(e);
      }
    }

    prepare();
  }, [fontsLoaded]);

  if (!fontsLoaded) {
    console.log("Fonts are not yet loaded.");
  } else {
    console.log("Fonts are loaded successfully.");
  }

  return (
    <FontsContext.Provider value={{ fontsLoaded }}>
      {fontsLoaded ? children : null}  
    </FontsContext.Provider>
  );
};
