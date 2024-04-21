import React from 'react';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import { StyleSheet } from 'react-native';
import { useTranslation } from 'react-i18next';
import { useTheme } from '../core/ThemeContext';
import Greetings from '../screens/auth/Greetings';
import SignUp from '../screens/auth/SignUp';
import SignIn from '../screens/auth/SignIn';

const Stack = createNativeStackNavigator();

function AuthStackNavigator() {
  const {t} = useTranslation();

  const { theme } = useTheme();

  return (
    <Stack.Navigator
    screenOptions={{
        headerStyle: { backgroundColor: theme.colors.background}, // Use the primary color from the theme
        headerTintColor: theme.colors.foreground, // Use the text color from the theme
        headerTitleStyle: { fontFamily: "merriweather-bold"}, // Use the font family for header text from the theme
  
      }}>
      <Stack.Screen name="Greeting" component={Greetings} options={{ title: t('GREETING') }} />
      <Stack.Screen name="Sign up" component={SignUp} options={{ title: t('SIGN_UP') }} />
      <Stack.Screen name="Sign in" component={SignIn} options={{ title: t('SIGN_IN') }} />
    </Stack.Navigator>
  );

}

export default AuthStackNavigator;
