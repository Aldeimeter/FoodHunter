// ThemeToggle.js
import React from 'react';
import { View, Switch, Text, StyleSheet } from 'react-native';
import { useTheme } from '../core/ThemeContext';
import { useTranslation } from 'react-i18next';

const ThemeToggle = () => {
    const { theme, toggleTheme } = useTheme();
    const isDark = theme.isDark;

    const {t} = useTranslation();
    
    return (
        <View style={styles.container}>
            <Text style={[styles.text, { color: theme.colors.foreground }]}>
              {t('MODE')}
            </Text>
            <Switch
                trackColor={{ false: theme.colors.foreground, true: theme.colors.primary }}
                thumbColor={isDark ? theme.colors.danger : theme.colors.success}
                ios_backgroundColor="#3e3e3e"
                onValueChange={toggleTheme}
                value={isDark}
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

export default ThemeToggle;
