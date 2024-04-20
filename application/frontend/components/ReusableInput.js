// ReusableInput.js 
// React stuff
import React, { useState } from 'react';
import { TextInput, View, Text, StyleSheet, TouchableOpacity } from 'react-native';
import { MaterialCommunityIcons } from '@expo/vector-icons';
// Theme stuff
import { useTheme } from '../core/ThemeContext';

const ReusableInput = ({
  style,
  onChangeText,
  value,
  placeholder,
  autoComplete,
  maxLength,
  secureTextEntry : initialSecureTextEntry,
  validateInput,
  inputType,
  label,
  labelStyle,
  isPassword,
}) => {
  const { theme } = useTheme();

  const [secureTextEntry, setSecureTextEntry] = useState(initialSecureTextEntry);
  const [error, setError] = useState('');

  // This function handles text change and validation
  const handleValidation = (text) => {
    let errorMessage = '';
    if (validateInput) {
      errorMessage = validateInput(text);
      setError(errorMessage);
    }
    onChangeText(text);
  };
  
  const togglePasswordVisibility = () => {
    setSecureTextEntry(!secureTextEntry);
  };

  const styles = createStyles(theme);

  const inputStyle = [
    styles.input,
    style,
    { borderColor: error ? theme.colors.danger : theme.colors.success }
  ];

  return (
    <View style={styles.container}>
      {label && <Text style={[styles.label, labelStyle]}>{label}</Text>}
      <View style={styles.inputRow}>
        <TextInput
          style={inputStyle}
          onChangeText={handleValidation}
          value={value}
          placeholder={placeholder}
          autoComplete={autoComplete}
          maxLength={maxLength}
          secureTextEntry={secureTextEntry}
          onSubmitEditing={() => handleValidation(value)}
        />
        {isPassword && (
            <TouchableOpacity onPress={togglePasswordVisibility} style={styles.icon}>
              <MaterialCommunityIcons
                name={secureTextEntry ? 'eye-off' : 'eye'}
                size={24}
                color={'#6e6869'}
              />
            </TouchableOpacity>
          )}
        </View>
      {error && <Text style={styles.errorText}>{error}</Text>}
    </View>
  );
};

const createStyles = (theme) => StyleSheet.create({
  container: {
    marginBottom: 20,
  },
  inputRow: {
    flexDirection: 'row',
    alignItems: 'center',
    alignSelf: 'center',
  },
  input: {
    height: 50,
    marginVertical: 10,
    paddingHorizontal: 10,
    borderWidth: 1.5,
    borderRadius: 12.5,
  },
  icon: {
    position: 'absolute',
    right: 10,
    padding: 5,
  },
  errorText: {
    paddingHorizontal: 10,
    fontSize: 12,
    textAlign: 'center',
  },
});

export default ReusableInput;
