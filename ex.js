import React, { useState } from 'react';
import { View, Text, TextInput } from 'react-native';

const MyStatefulComponent = () => {
  const [text, setText] = useState('');

  return (
    <View>
      <TextInput
        placeholder="Type here"
        onChangeText={newText => setText(newText)}
        value={text}
      />
      <Text>You typed: {text}</Text>
    </View>
  );
};

export default MyStatefulComponent;