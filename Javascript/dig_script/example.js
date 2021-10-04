const data = {
    level1: {
      level2: {
        level3: 'some data'
      }
    }
  };
  dig(data, 'level3'); // 'some data'
  dig(data, 'level4'); // undefined