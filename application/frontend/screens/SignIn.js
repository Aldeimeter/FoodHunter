// SignIn.js
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
// encrypted storage 
import { save, get } from '../core/userDataStorage';

function SignIn ({ navigation }) {
  const { theme } = useTheme();

  const styles = createStyles(theme);

  const {t} = useTranslation();

  const windowWidth = Dimensions.get('window').width;

  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const [emailValid, setEmailValid] = useState(false);
  const [passwordValid, setPasswordValid] = useState(false);

  const [message, setMessage] = useState('');
  

  const handleSignIn = () => {
    const isEmailValid = !validateEmail(email.trim());
    const isPasswordValid = !validatePassword(password.trim());

    setEmailValid(isEmailValid);
    setPasswordValid(isPasswordValid);
    setMessage('');

    if (!emailValid || !passwordValid) {
      console.log(emailValid);
      console.log(passwordValid);
      setMessage(t('INVALID_FORMAT'));
      return; // Exit the function early
    }
    const payload = {
      username: email.toLowerCase(),
      password: password.trim(),
    };


    const params = Object.keys(payload).map(key => encodeURIComponent(key) + '=' + encodeURIComponent(payload[key])).join('&');

    fetch(base_url + '/auth/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json'
      },
      body: params
    })
    .then(response => {
      if (!response.ok) {
        const error = response.headers.get('app-error')
        throw new Error(t(error) || t('SIGN_IN_FAILURE'));
      }
      return response.json();
    })
    .then(async (data) => {
      console.log(data);
      await save(data['token_type'], data['access_token']);
      await save('refresh_token',data['refresh_token']);
      navigation.navigate('Greeting')   
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
        placeholder={t("PASSWORD_INPUT")}
        autoComplete="current-password"
        maxLength={255}
        secureTextEntry={true}
        validateInput={validatePassword}
        isPassword={true}
        />
        <TouchableOpacity style={[styles.button, { width: windowWidth * 0.7 }]} onPress={() => handleSignIn()} >
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


export default SignIn;
