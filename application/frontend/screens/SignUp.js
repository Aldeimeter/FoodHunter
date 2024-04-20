// SignUp.js
// React stuff
import React, { useState } from 'react';
import { TouchableOpacity, Text, TextInput, View, StyleSheet, Dimensions } from 'react-native';
// Language stuff
import { useTranslation } from 'react-i18next';
// Theme stuff
import { useTheme } from '../core/ThemeContext';
// Own components 
import ReusableInput from '../components/ReusableInput';
// Validation functions 
import { validateEmail, validatePassword, validatePasswordMatch} from '../core/validation';
// base_url 
import { base_url } from '../core/config';

function SignUp({ navigation }) {
  const { theme } = useTheme();

  const styles = createStyles(theme);

  const {t} = useTranslation();

  const windowWidth = Dimensions.get('window').width;

  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [passwordAgain, setPasswordAgain] = useState('');

  const [emailValid, setEmailValid] = useState(false);
  const [passwordValid, setPasswordValid] = useState(false);
  const [passwordAgainValid, setPasswordAgainValid] = useState(false);

  const [message, setMessage] = useState('');
  
  const checkEmailValid = (text) => {
    const valid = validateEmail(text);
    setEmailValid(!valid); // assuming validateEmail returns an empty string if valid
    setEmail(text);
  };

  const checkPasswordValid = (text) => {
    const valid = validatePassword(text);
    setPasswordValid(!valid);
    setPassword(text);
  };

  const checkPasswordAgainValid = (text) => {
    const valid = validatePasswordMatch(password, text);
    setPasswordAgainValid(!valid);
    setPasswordAgain(text);
  };

  const handleSignUp = () => {
    checkEmailValid(email.trim());
    checkPasswordValid(password.trim());
    checkPasswordAgainValid(passwordAgain.trim());
    setMessage('');

    if (!emailValid || !passwordValid) {
      setMessage(t('INVALID_FORMAT'));
      return; // Exit the function early
    }
    if (!passwordAgainValid) {
      setMessage(t('PASSWORDS_NOT_MATCH'));
      return; // Exit the function early
    }

    const payload = {
      email: email.toLowerCase(),
      password: password.trim(),
    };

    fetch(base_url + '/auth/register', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
      },
      body: JSON.stringify(payload)
    })
    .then(response => {
      if (!response.ok) {
        const error = response.headers.get('app-error')
        throw new Error(t(error) || t('SIGN_UP_FAILURE'));
      }
      return response.json();
    })
    .then(data => {
      console.log(data);
      // storeUserData(data);
      // navigation.navigate('Home');
    })
    .catch(error => {
      console.error(error);
      setMessage(error.message);
    });
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
