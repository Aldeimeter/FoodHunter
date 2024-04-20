import i18n from 'i18next';

export const validateEmail = (email) => {
  const re = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
  return re.test(email) ? '' : i18n.t('INVALID_EMAIL_FORMAT');
};

export const validatePassword = (password) => {
  const re = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d!@#$%^&*]{8,}$/;
  return re.test(password) ? '' : i18n.t('PASSWORD_REQUIREMENTS');
};

export const validatePasswordMatch = (password, confirmPassword) => {
  return password === confirmPassword ? '' : i18n.t('PASSWORDS_NOT_MATCH');
};
