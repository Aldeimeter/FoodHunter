// ./navigation/MainStackNavigator.js
import React from 'react';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import { StyleSheet } from 'react-native';
import { useTranslation } from 'react-i18next';
import { useTheme } from '../core/ThemeContext';
import Home from '../screens/main/Home';
import SignUp from '../screens/auth/SignUp';
import SignIn from '../screens/auth/SignIn';

const Stack = createNativeStackNavigator();

function MainStackNavigator() {
  const {t} = useTranslation();

  const { theme } = useTheme();

  return (
    <Stack.Navigator
    screenOptions={{
        headerStyle: { backgroundColor: theme.colors.background}, // Use the primary color from the theme
        headerTintColor: theme.colors.foreground, // Use the text color from the theme
        headerTitleStyle: { fontFamily: "merriweather-bold"}, // Use the font family for header text from the theme
  
      }}>
      <Stack.Screen name="Home" component={Home} options={{ title: t('GREETING') }} />
    </Stack.Navigator>
  );

}

export default MainStackNavigator;
