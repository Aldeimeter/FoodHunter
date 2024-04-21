// Greetings.js
// React stuff
import React from 'react';
import { TouchableOpacity, Text, View, StyleSheet, Dimensions } from 'react-native';
// Language stuff
import { useTranslation } from 'react-i18next';
import LanguageToggle from "../../components/LanguageToggle";
// Theme stuff
import { useTheme } from '../../core/ThemeContext';
import ThemeToggle from '../../components/ThemeToggle';
//
import {base_url} from '../../core/config'

function Greetings({ navigation }) {
  const { theme } = useTheme();

  const styles = createStyles(theme);

  const {t} = useTranslation();

  return (
      <View style={styles.container}>
        <TouchableOpacity style={[styles.button, { width: Dimensions.get('window').width * 0.7 }]} onPress={() => navigation.navigate('Sign in')}>
          <Text style={styles.buttonText}>{t('SIGN_IN')}</Text>
        </TouchableOpacity>
        <TouchableOpacity style={[styles.button, { width: Dimensions.get('window').width * 0.7 }]} onPress={() => navigation.navigate('Sign up')} >
          <Text style={styles.buttonText}>{t('SIGN_UP')}</Text>
        </TouchableOpacity>
        <View style={styles.settingsContainer}>
          <ThemeToggle />
          <LanguageToggle/>
        </View>
      </View>
  );
}

const createStyles = (theme) => StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: theme.colors.background,
  },
  settingsContainer: {
    flexDirection: 'row',
    justifyContent: 'center',
    alignItems: 'center',
  },
  text: {
    color: theme.colors.secondary,
    fontSize: 24,
    fontFamily: theme.textVariants.body.fontFamily,
    marginBottom: 20,
  },
  button: {
    backgroundColor: theme.colors.primary,
    paddingVertical: 12,
    paddingHorizontal: 24,
    borderRadius: 8,
    marginBottom: 16,
    borderWidth: 1,
    borderColor: theme.colors.secondary,
  },
  buttonText: {
    color: theme.colors.secondary,
    fontSize: 16,
    fontFamily: theme.textVariants.body.fontFamily,
    textAlign: 'center',
  },
});

export default Greetings;
