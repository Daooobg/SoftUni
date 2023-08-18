import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'capitalizeAll',
})
export class CapitalizeAllWordsPipe implements PipeTransform {
  transform(value: string): string {
    if (!value) return '';
    const words = value.split(' ');
    const capitalizedWords = words.map(
      (word) => word.charAt(0).toUpperCase() + word.slice(1).toLowerCase()
    );
    return capitalizedWords.join(' ');
  }
}
