import React from 'react';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import { StyleSheet } from 'react-native';
import { useTranslation } from 'react-i18next';
import { useTheme } from '../core/ThemeContext';
import HomeScreen from '../screens/HomeScreen';

const Stack = createNativeStackNavigator();

function StackNavigator() {
  const {t} = useTranslation();

  const { theme } = useTheme();

  return (
    <Stack.Navigator
    screenOptions={{
        headerStyle: { backgroundColor: theme.colors.background}, // Use the primary color from the theme
        headerTintColor: theme.colors.foreground, // Use the text color from the theme
        headerTitleStyle: { fontFamily: "merriweather-bold"}, // Use the font family for header text from the theme
  
      }}>
      <Stack.Screen name="Home" component={HomeScreen} options={{ title: t('GREETING') }} />
    </Stack.Navigator>
  );

}

export default StackNavigator;
