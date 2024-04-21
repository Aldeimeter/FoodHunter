// SignUp.js
// React stuff
import React, { useState } from 'react';
import { TouchableOpacity, Text, TextInput, View, StyleSheet, Dimensions } from 'react-native';
// Language stuff
import { useTranslation } from 'react-i18next';
// Theme stuff
import { useTheme } from '../../core/ThemeContext';
// Own components 
import ReusableInput from '../../components/ReusableInput';
// Validation functions 
import { validateEmail, validatePassword, validatePasswordMatch} from '../../core/validation';
// userService import 
import { registerUser } from '../../api/userService';
// Loading scene stuff 
import { useLoading } from '../../core/LoadingContext';

function SignUp({ navigation }) {
  const { theme } = useTheme();

  const styles = createStyles(theme);

  const {t} = useTranslation();

  const windowWidth = Dimensions.get('window').width;

  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [passwordAgain, setPasswordAgain] = useState('');

  const [message, setMessage] = useState('');
  
  const { showLoading, hideLoading } = useLoading();

  const handleSignUp = async () => {
    try {
        const isEmailValid = !validateEmail(email.trim());
        const isPasswordValid = !validatePassword(password.trim());
        const isPasswordsMatch = !validatePasswordMatch(password.trim(), passwordAgain.trim());
        if (!isEmailValid || !isPasswordValid || !isPasswordsMatch) {
            const errorMessage = !isEmailValid ? t('INVALID_FORMAT') :
                                 !isPasswordValid ? t('INVALID_FORMAT') :
                                 t('PASSWORDS_NOT_MATCH');
            setMessage(errorMessage);
            return;
        }

        showLoading();
        const userData = await registerUser(email, password);
        hideLoading();
        console.log('User registered:', userData);
    } catch (error) {
        console.error('Registration failed:', error);
        setMessage(t(error.message));
        hideLoading();
    }
  };

  return (
      <View style={styles.container}>
        <ReusableInput
        style={[styles.input, { width: windowWidth * 0.7 }]}
        onChangeText={setEmail}
        value={email}
        placeholder={t("EMAIL_INPUT")}
        autoComplete="email"
        maxLength={255}
        validateInput={validateEmail}
        />
        <ReusableInput
        style={[styles.input, { width: windowWidth * 0.7 }]}
        onChangeText={setPassword}
        value={password}
        placeholder={t("PASSWORD_CREATE_INPUT")}
        autoComplete="new-password"
        maxLength={255}
        secureTextEntry={true}
        validateInput={validatePassword}
        isPassword={true}
        />
        <ReusableInput
        style={[styles.input, { width: windowWidth * 0.7 }]}
        onChangeText={setPasswordAgain}
        value={passwordAgain}
        placeholder={t("PASSWORD_AGAIN_INPUT")}
        autoComplete="new-password"
        maxLength={255}
        secureTextEntry={true}
        isPassword={true}
        />
        <TouchableOpacity style={[styles.button, { width: windowWidth * 0.7 }]} onPress={() => handleSignUp()} >
          <Text style={styles.buttonText}>{t('SIGN_IN')}</Text>
        </TouchableOpacity>
      {message && <Text>{message}</Text>}
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


export default SignUp;
