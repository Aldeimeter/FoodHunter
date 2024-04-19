// LanguageToggle.js
import React from 'react';
import { View, Switch, Text, StyleSheet } from 'react-native';
import { useLanguage } from '../core/LanguageContext';
import { useTheme } from '../core/ThemeContext';
import { useTranslation } from 'react-i18next';

const LanguageToggle = () => {
    const { selectedLanguage, changeLanguage } = useLanguage();
    const { theme } = useTheme();

    const {t} = useTranslation();

    const toggleLanguage = () => {
        const newLanguage = selectedLanguage === 'en' ? 'sk' : 'en'; // Toggle between English and Slovak
        changeLanguage(newLanguage);
    };

    return (
        <View style={styles.container}>
            <Text style={[styles.text, { color: theme.colors.foreground }]}>
              {t("LANGUAGE")}  
            </Text>
            <Switch
                trackColor={{ false: theme.colors.foreground, true: theme.colors.primary }}
                thumbColor={theme.colors.text}
                ios_backgroundColor="#3e3e3e"
                onValueChange={toggleLanguage}
                value={selectedLanguage === 'en'} 
            />
        </View>
    );
};

const styles = StyleSheet.create({
    container: {
        flexDirection: 'row',
        alignItems: 'center',
        justifyContent: 'space-between',
        padding: 10,
        marginVertical: 10,
    },
    text: {
        fontSize: 18,
        fontWeight: '500',
    },
});

export default LanguageToggle;
