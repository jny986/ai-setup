import { onMounted, onUnmounted } from 'vue';
import { onContentUpdated } from 'vitepress';

// VitePress owns copying and the temporary `copied` class. The custom theme
// supplies real button text so labels and feedback do not depend on its CSS.
export function useCodeCopyFeedback() {
  let observer: MutationObserver | undefined;

  function update(button: HTMLButtonElement) {
    button.textContent = button.classList.contains('copied') ? 'Copied!' : 'Copy';
  }

  function enhance() {
    observer?.disconnect();
    observer = new MutationObserver(records => {
      for (const record of records) update(record.target as HTMLButtonElement);
    });
    for (const button of document.querySelectorAll<HTMLButtonElement>('div[class*="language-"] > button.copy')) {
      button.type = 'button';
      button.setAttribute('aria-label', 'Copy code');
      button.setAttribute('aria-live', 'polite');
      update(button);
      observer.observe(button, { attributes: true, attributeFilter: ['class'] });
    }
  }

  onMounted(enhance);
  onContentUpdated(enhance);
  onUnmounted(() => observer?.disconnect());
}
