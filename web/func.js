function getGroupUrl() {
  const url_list = [];
  const urls = document.getElementsByName("group_url");
  const urls_len = urls.length;

  for (let i = 0; i < urls_len; i++) {
        url_list.push(urls[i].value)
    }
    eel.get_input_url(url_list);
}