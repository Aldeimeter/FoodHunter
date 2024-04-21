import * as SecureStore from 'expo-secure-store';
export const save = async (key, value) =>{
 try {
  await SecureStore.setItemAsync(key, value);
 } catch (error) {
    console.error(error);  
 }
}

export const get = async (key) => {
  let result = await SecureStore.getItemAsync(key);
  if (result) {
      return result;
  } else {
    throw new Error("No value for this key.");
  }
}
export const remove = async (key) => {
  try {
    await SecureStore.deleteItemAsync(key);
  } catch (error) {
    throw new Error (`Failed to remove item from SecureStore: ${error}`);
  }
};
