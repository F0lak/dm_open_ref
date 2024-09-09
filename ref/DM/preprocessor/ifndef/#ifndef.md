[]{#/DM/preprocessor/ifndef}
  ## #ifndef directive
  **See also:**
  :   [#define directive](ref/DM/preprocessor/define)
  :   [#if directive](ref/DM/preprocessor/if)
  :   [#ifdef directive](ref/DM/preprocessor/ifdef)
  :   [preprocessor](ref/DM/preprocessor)
  <!-- -->
  **Format:**
  :   #ifndef Name
  <!-- -->
  **Args:**
  :   Name: A macro definition.
  The `#ifndef` statement is used to conditionally compile code. It is
  equivalent to `#if !defined(Name)`.